from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


group_env = db.Table('group_env',
    db.Column('group_id', db.Integer, db.ForeignKey('group.group_id')),
    db.Column('env_id', db.Integer, db.ForeignKey('env.env_id'))
)

group_bu = db.Table('group_bu',
    db.Column('group_id', db.Integer, db.ForeignKey('group.group_id')),
    db.Column('bu_id', db.Integer, db.ForeignKey('bu.bu_id'))
)

group_app = db.Table('group_app',
    db.Column('group_id', db.Integer, db.ForeignKey('group.group_id')),
    db.Column('app_id', db.Integer, db.ForeignKey('app.app_id'))
)

group_host = db.Table('group_host',
    db.Column('group_id', db.Integer, db.ForeignKey('group.group_id')),
    db.Column('host_id', db.Integer, db.ForeignKey('host.host_id'))
)

class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(20), unique=True
)

class Env(db.Model):
    env_id = db.Column(db.Integer, primary_key=True)
    env_name = db.Column(db.String(20), unique=True)
    env_sub  = db.relationship('Group', secondary=group_env, backref=db.backref('envs', lazy='dynamic')
)

class Bu(db.Model):
    bu_id = db.Column(db.Integer, primary_key=True)
    bu_name = db.Column(db.String(20), unique=True)
    bu_sub  = db.relationship('Group', secondary=group_bu, backref=db.backref('bus', lazy='dynamic')
)

class App(db.Model):
    app_id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(20), unique=True)
    app_sub  = db.relationship('Group', secondary=group_app, backref=db.backref('apptype', lazy='dynamic')
)

class Host(db.Model):
    host_id = db.Column(db.Integer, primary_key=True)
    host_name = db.Column(db.String(20), unique=True)
    host_sub  = db.relationship('Group', secondary=group_host, backref=db.backref('host', lazy='dynamic')
)
