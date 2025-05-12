import matplotlib
matplotlib.use('Agg')
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from .forms import TransactionForm, LimitForm, UploadForm
from .models import Transaction, Limit
from . import db
from sqlalchemy import func
import os
import pandas as pd
from werkzeug.utils import secure_filename
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ekle', methods=['GET', 'POST'])
def add_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        tx = Transaction(
            type=form.type.data,
            category=form.category.data.lower(),
            amount=form.amount.data
        )
        db.session.add(tx)
        db.session.commit()
        flash("İşlem eklendi", "success")
        return redirect(url_for('main.summary'))
    return render_template('add_transaction.html', form=form)

@main.route('/limits', methods=['GET', 'POST'])
def set_limit():
    form = LimitForm()
    limits = Limit.query.all()
    if form.validate_on_submit():
        existing = Limit.query.filter_by(category=form.category.data.lower()).first()
        if existing:
            existing.limit = form.limit.data
        else:
            db.session.add(Limit(category=form.category.data.lower(), limit=form.limit.data))
        db.session.commit()
        flash("Limit güncellendi.", "success")
        return redirect(url_for('main.set_limit'))
    return render_template('limits.html', form=form, limits=limits)

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        print("✅ Form gönderildi.")
        file = form.file.data
        print(f"📄 Dosya adı: {file.filename}")
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

        # Eksikse uploads klasörünü oluştur
        if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
            os.makedirs(current_app.config['UPLOAD_FOLDER'])

        file.save(filepath)
        print(f"📂 Kaydedilen yol: {filepath}")
        try:
            # xls için engine belirt
            if filename.endswith('.xls'):
                df = pd.read_excel(filepath, engine='xlrd')
            else:
                df = pd.read_excel(filepath)

            required_cols = ['Tarih', 'Açıklama', 'Tutar']
            for col in required_cols:
                if col not in df.columns:
                    raise ValueError(f"'{col}' sütunu eksik!")

            df['Tarih'] = pd.to_datetime(df['Tarih'], errors='coerce')
            df['Tutar'] = pd.to_numeric(df['Tutar'], errors='coerce')
            df = df.dropna(subset=['Tarih', 'Tutar'])

            df['Tür'] = df['Tutar'].apply(lambda x: 'gelir' if x > 0 else 'gider')
            df['Kategori'] = df['Açıklama'].fillna('diğer').str.lower()

            for _, row in df.iterrows():
                tx = Transaction(
                    type=row['Tür'],
                    category=row['Kategori'],
                    amount=abs(row['Tutar']),
                    date=row['Tarih']
                )
                db.session.add(tx)
            db.session.commit()
            flash("Dosya başarıyla içe aktarıldı.", "success")
            return redirect(url_for('main.summary'))

        except Exception as e:
            flash(f"Yükleme hatası: {e}", "danger")

    return render_template('upload.html', form=form)

@main.route('/ozet')
def summary():
    income = db.session.query(func.sum(Transaction.amount)).filter_by(type='gelir').scalar() or 0
    expense = db.session.query(func.sum(Transaction.amount)).filter_by(type='gider').scalar() or 0
    balance = income - expense

    warnings = []
    for limit in Limit.query.all():
        total = db.session.query(func.sum(Transaction.amount))\
            .filter_by(type='gider', category=limit.category).scalar() or 0
        if total > limit.limit:
            warnings.append(f"⚠️ {limit.category} harcaması limiti ({limit.limit}₺) aştı: {total}₺")

    transactions = Transaction.query.all()
    df = pd.DataFrame([{
        "Tarih": t.date,
        "Kategori": t.category,
        "Tutar": t.amount if t.type == 'gelir' else -t.amount,
        "Tür": t.type
    } for t in transactions])

    monthly_plot, category_plot = None, None
    if not df.empty:
        df['Tarih'] = pd.to_datetime(df['Tarih'])
        df['Ay'] = df['Tarih'].dt.to_period('M')
        monthly = df.groupby(['Ay', 'Tür'])['Tutar'].sum().unstack().fillna(0)

        fig1, ax1 = plt.subplots()
        monthly.plot(kind='bar', ax=ax1, title='Aylık Gelir-Gider')
        plt.tight_layout()
        buf1 = BytesIO()
        fig1.savefig(buf1, format='png')
        buf1.seek(0)
        monthly_plot = base64.b64encode(buf1.read()).decode('utf-8')

        giderler = df[df['Tür'] == 'gider']
        category_sum = giderler.groupby('Kategori')['Tutar'].sum().abs()
        fig2, ax2 = plt.subplots()
        category_sum.plot(kind='pie', autopct='%1.1f%%', ax=ax2, title='Kategori Bazlı Gider Dağılımı')
        ax2.set_ylabel('')
        plt.tight_layout()
        buf2 = BytesIO()
        fig2.savefig(buf2, format='png')
        buf2.seek(0)
        category_plot = base64.b64encode(buf2.read()).decode('utf-8')

    return render_template('summary.html',
                           income=income,
                           expense=expense,
                           balance=balance,
                           warnings=warnings,
                           monthly_plot=monthly_plot,
                           category_plot=category_plot)
