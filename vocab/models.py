# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
#from sqlalchemy import desc
from . import db


# ================================================================
class VocabItem(db.Model):
    __tablename__ = 'vocabulary'
    idw = db.Column(db.Integer, primary_key = True)
    word = db.Column(db.Unicode(100), index = True, unique = True)
    translation = db.Column(db.Unicode(100), nullable = False, index = True)
    note = db.Column(db.Text)
    
    @staticmethod
    def newest(num):
        return VocabItem.query.order_by(VocabItem.word).limit(num)
    
    @staticmethod
    def allRecords():
        return VocabItem.query.order_by(VocabItem.word).all()
    
    
    def __unicode__(self):
        return self.word
    
    
    def __repr__(self):
        return '<Word: {}, translation: {}>'.format(self.word, self.translation)


# ================================================================
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    idu = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Unicode(50), index = True, unique = True)
    password_hash = db.Column(db.Unicode(70))
    
    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def register(username, password):
        user = User(username = username)
        user.password = password
        db.session.add(user)
        db.session.commit()
        
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username = username).first()

    def __repr__(self):
        return '<User {0}>'.format(self.username)
    
    def get_id(self):
        """
        Assuming that the user object has an `idu` attribute, this will take
        that and convert it to `unicode`.
        """
        try:
            return self.idu
        except AttributeError:
            raise NotImplementedError("No 'idu' attribute - override get_id")    
    
