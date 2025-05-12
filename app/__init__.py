from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import Config

csrf = CSRFProtect()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    csrf.init_app(app)
    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app