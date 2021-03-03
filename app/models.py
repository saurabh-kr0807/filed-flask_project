# -*- coding: utf-8 -*-

from datetime import datetime
from app import db

class Song(db.Model):

    '''This class represents the song table'''
    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime, default=datetime.now)

    # def __init__(self, name):
    #     '''initialize with name'''
    #     self.name = name

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    # @staticmethod
    # def get_all():
    #     return Song.query.all()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()

class Podcast(db.Model):
    
    '''This class represents the Podcast table'''
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime, default=datetime.now)
    host = db.Column(db.String(100))
    participants = db.Column(db.String)




class Audiobook(db.Model):
    
    '''This class represents the Audiobook table'''
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    narrator = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime, default=datetime.now)
