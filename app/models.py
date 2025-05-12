from . import db
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # gelir/gider
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)

class Limit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), unique=True)
    limit = db.Column(db.Float)