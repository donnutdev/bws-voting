from . import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


class ViceHeadBoy(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHeadGirl(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceSportsCaptain(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceCulturalHead(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHouseCaptainSpartans(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHouseCaptainKnights(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHouseCaptainTrojans(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class ViceHouseCaptainSamurais(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)

# yesss
class HeadBoy(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class HeadGirl(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class SportsCaptain(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class CulturalHead(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class HouseCaptainSpartans(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class HouseCaptainKnights(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class HouseCaptainTrojans(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)


class HouseCaptainSamurais(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    grade = db.Column(db.String(), nullable=False)
    vote_choice = db.Column(db.String(), nullable=False)
