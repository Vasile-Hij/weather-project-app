#!/usr/bin/env python3
from flask_login import UserMixin
from project import db, login_manager


@login_manager.user_loader
def load_user(username):
    return User.query.get(int(username))


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=False)
    user_city = db.relationship("UserToCityMapping", backref="city_searched", lazy=True, cascade="all, delete", passive_deletes=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User('{self.username}', '{self.email})"


class UserToCityMapping(db.Model):
    __tablename__ = "user_to_city_mapping"
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    def __init__(self, city_name, user_id):
        self.city_name = city_name
        self.user_id = user_id


    def __repr__(self):
        return f"UserToCityMapping('{self.city_name}', '{self.user_id}')"
