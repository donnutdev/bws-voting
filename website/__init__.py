from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "111111111"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    from .models import ViceHeadBoy, ViceHeadGirl, ViceSportsCaptain, ViceCulturalHead,\
        ViceHouseCaptainSpartans, ViceHouseCaptainKnights,\
        ViceHouseCaptainTrojans, ViceHouseCaptainSamurais, User, \
        HeadBoy, HeadGirl, SportsCaptain, CulturalHead, \
        HouseCaptainSpartans, HouseCaptainKnights, \
        HouseCaptainTrojans, HouseCaptainSamurais
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'views.authorize'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database Initialized")
