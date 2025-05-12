from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class TransactionForm(FlaskForm):
    type = SelectField('Tür', choices=[('gelir', 'Gelir'), ('gider', 'Gider')], validators=[DataRequired()])
    category = StringField('Kategori', validators=[DataRequired()])
    amount = FloatField('Tutar (₺)', validators=[DataRequired()])
    submit = SubmitField('Kaydet')

class LimitForm(FlaskForm):
    category = StringField('Kategori', validators=[DataRequired()])
    limit = FloatField('Limit (₺)', validators=[DataRequired()])
    submit = SubmitField('Kaydet / Güncelle')

class UploadForm(FlaskForm):
    file = FileField('Excel Dosyası (.xlsx, .csv)', validators=[FileAllowed(['xlsx', 'csv'], 'Sadece Excel dosyası!')])
    submit = SubmitField('Yükle')