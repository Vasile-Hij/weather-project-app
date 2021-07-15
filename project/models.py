#!/bin/usr/env python3
from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, email, name, password):
        self.email = email
        self.password = password
        self.name = name


class UserToCityMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
