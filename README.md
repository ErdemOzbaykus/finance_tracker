# 📊 Kişisel Finans Takip Uygulaması (Flask)

Bu proje, kişisel gelir ve giderlerinizi takip edebileceğiniz, harcama limitleri belirleyebileceğiniz ve Excel banka dökümlerinizi içe aktarabileceğiniz bir web uygulamasıdır. Flask framework'ü kullanılarak geliştirilmiştir.

---

## 🚀 Özellikler

✅ Gelir ve gider ekleme  
✅ Aylık grafiklerle finansal özet (Matplotlib)  
✅ Kategori bazlı harcama dağılımı  
✅ Harcama limiti tanımlama ve aşım uyarısı  
✅ Excel/CSV banka dökümü yükleme (Pandas ile)  
✅ SQLite ile veritabanı yönetimi  
✅ Flask tabanlı web arayüzü

---

## ⚙️ Kurulum

### 1. Projeyi klonlayın veya indirin
```bash
git clone https://github.com/kullaniciadi/finance_tracker.git
cd finance_tracker
```

### 2. Sanal ortam oluşturun
```bash
python3 -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
```

### 3. Gereksinimleri yükleyin
```bash
pip install -r requirements.txt
```

### 4. Uygulamayı başlatın
```bash
python app.py
```

Tarayıcınızda `http://127.0.0.1:5000/` adresine giderek uygulamayı kullanabilirsiniz.

---

## 📁 Proje Klasör Yapısı

```
finance_tracker/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── add_transaction.html
│   │   ├── summary.html
│   │   ├── limits.html
│   │   └── upload.html
│   └── static/
├── uploads/                ← Excel dosyaları buraya gelir
├── finance.db              ← SQLite veritabanı
├── requirements.txt
├── app.py
└── README.md
```

---

## 🧪 Kullanılan Teknolojiler

- Flask
- Flask-WTF (formlar için)
- SQLAlchemy (veritabanı ORM)
- Pandas (Excel/CSV okuma)
- Matplotlib (grafik çizimi)
- HTML5 (template yapısı)

---

## 📸 Ekran Görüntüleri

> (İsteğe bağlı: `static/` klasörüne grafiklerin PNG çıktısını koyup aşağıya ekleyebilirsin)

---

## 📬 Katkıda Bulunmak

Her türlü geri bildirime açığım. Fork'layıp kendi versiyonunu oluşturabilir, yeni özellikler ekleyebilirsin.

---

## 📝 Lisans

Bu proje kişisel kullanım için geliştirilmiştir. Herhangi bir ticari amaçla dağıtılmadan önce geliştiriciye bildirilmesi tavsiye edilir.


---


# 📊 Personal Finance Tracker (Flask)

This project is a web application to track your income and expenses, set spending limits, and import your bank statements in Excel format. Built using the Flask framework.

---

## 🚀 Features

✅ Add income and expenses  
✅ Monthly financial summary with charts (Matplotlib)  
✅ Expense breakdown by category  
✅ Set spending limits with alerts  
✅ Import bank statements (Excel/CSV via Pandas)  
✅ Data stored using SQLite  
✅ Web interface powered by Flask

---

## ⚙️ Installation

### 1. Clone or download the project
```bash
git clone https://github.com/yourusername/finance_tracker.git
cd finance_tracker
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

Access the app at `http://127.0.0.1:5000/` in your browser.

---

## 📁 Project Structure

Same as Turkish version (see above).

---

## 🧪 Technologies Used

- Flask
- Flask-WTF
- SQLAlchemy
- Pandas
- Matplotlib
- HTML5

---

## 📸 Screenshots

> Optionally add images in the `static/` folder and embed here.

---

## 📬 Contribution

Feel free to fork this project, suggest improvements or open issues.

---

## 📝 License

For personal use only. Please contact the author for commercial use.


---


# 📊 Persönlicher Finanzmanager (Flask)

Dieses Projekt ist eine Webanwendung zur Verwaltung deiner Einnahmen und Ausgaben. Du kannst Ausgabenlimits setzen und Excel-Bankauszüge importieren. Entwickelt mit dem Flask-Framework.

---

## 🚀 Funktionen

✅ Einnahmen und Ausgaben erfassen  
✅ Monatliche Finanzübersicht mit Diagrammen (Matplotlib)  
✅ Ausgaben nach Kategorien aufgeschlüsselt  
✅ Ausgabenlimits festlegen + Warnungen  
✅ Excel/CSV-Bankauszüge importieren (Pandas)  
✅ SQLite-Datenbank  
✅ Flask-Weboberfläche

---

## ⚙️ Installation

### 1. Projekt klonen oder herunterladen
```bash
git clone https://github.com/yourusername/finance_tracker.git
cd finance_tracker
```

### 2. Virtuelle Umgebung erstellen
```bash
python3 -m venv venv
source venv/bin/activate  # Unter Windows: venv\Scripts\activate
```

### 3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 4. Anwendung starten
```bash
python app.py
```

Die Anwendung läuft unter `http://127.0.0.1:5000/`.

---

## 📁 Projektstruktur

Siehe türkische Version oben.

---

## 🧪 Verwendete Technologien

- Flask  
- Flask-WTF  
- SQLAlchemy  
- Pandas  
- Matplotlib  
- HTML5

---

## 📸 Bildschirmfotos

> Optional Bilder in `static/` ablegen und hier einfügen.

---

## 📬 Beitrag leisten

Du kannst das Projekt forken, erweitern oder Feedback geben.

---

## 📝 Lizenz

Nur für privaten Gebrauch. Für kommerzielle Nutzung bitte den Autor kontaktieren.
