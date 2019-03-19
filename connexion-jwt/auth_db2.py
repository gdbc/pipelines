from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_env = db.Table('user_env',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('env_id', db.Integer, db.ForeignKey('env.env_id'))
)

user_bu = db.Table('user_bu',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('bu_id', db.Integer, db.ForeignKey('bu.bu_id'))
)

user_app = db.Table('user_app',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('app_id', db.Integer, db.ForeignKey('app.app_id'))
)

user_host = db.Table('user_host',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('host_id', db.Integer, db.ForeignKey('host.host_id'))
)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True
)

class Env(db.Model):
    env_id = db.Column(db.Integer, primary_key=True)
    env_name = db.Column(db.String(20), unique=True)
    env_sub  = db.relationship('User', secondary=user_env, backref=db.backref('envs', lazy='dynamic')
)

class Bu(db.Model):
    bu_id = db.Column(db.Integer, primary_key=True)
    bu_name = db.Column(db.String(20), unique=True)
    bu_sub  = db.relationship('User', secondary=user_bu, backref=db.backref('bus', lazy='dynamic')
)

class App(db.Model):
    app_id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(20), unique=True)
    app_sub  = db.relationship('User', secondary=user_app, backref=db.backref('apptype', lazy='dynamic')
)

class Host(db.Model):
    host_id = db.Column(db.Integer, primary_key=True)
    host_name = db.Column(db.String(20), unique=True)
    host_sub  = db.relationship('User', secondary=user_host, backref=db.backref('host', lazy='dynamic')
)
