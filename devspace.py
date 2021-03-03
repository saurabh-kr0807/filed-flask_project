#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:21:35 2021

@author: somitsinha
"""
from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime, default=datetime.now)

class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime, default=datetime.now)
    host = db.Column(db.String(100))
    participants = db.Column(db.String)

class Audiobook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    narrator = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime, default=datetime.now)

# db.create_all()


@app.route('/<audioFileType>/', methods=['GET','POST'])
def get_insert_data(audioFileType):

    if request.method=='GET':
        if audioFileType=='Song':
            songs = Song.query.all()
            return render_template('list.html', songs=songs)
        elif audioFileType == "Podcast":
            podcast = Podcast.query.all()
            return render_template('list.html', podcast=podcast)
        elif audioFileType == "Audiobook":
            audiobook = Audiobook.query.all()
            return render_template('list.html', audiobook=audiobook)

    if request.method=='POST':
        if audioFileType=='Song':
            data = request.get_json()
            name = data['name']
            duration = data['duration']
            # upload_time = data['upload_time']
            song = Song(name=name, duration=duration)
            db.session.add(song)
            db.session.commit()
            return '<h1>successful songs added: 200 OK</h1>'

        elif audioFileType=='Podcast':
            data = request.get_json()
            name = data['name']
            duration = data['duration']
            host = data['host']
            participants = data['participants']
            # upload_time = data['upload_time']
            podcast = Podcast(name=name, duration=duration, host=host, participants=participants)
            db.session.add(podcast)
            db.session.commit()
            return '<h1>successful podcast added: 200 OK</h1>'

        elif audioFileType=='Audiobook':
            data = request.get_json()
            title = data['title']
            author = data['author']
            narrator = data['narrator']
            duration = data['duration']
            # upload_time = data['upload_time']
            audiobook = Audiobook(title=title, author=author, narrator=narrator,duration=duration)
            db.session.add(audiobook)
            db.session.commit()
            return '<h1>successful audiobook added: 200 OK</h1>'

@app.route('/<audioFileType>/<audioFileID>', methods=['GET','PUT','DELETE'])
def get_update_delete_data(audioFileType, audioFileID):

    if request.method=='GET' and audioFileType=='Song':
        song = Song.query.filter_by(id=audioFileID).first()
        return f'<h1>Song name is { song.name } and runtime is { song.duration }</h1>'

    if request.method=='GET' and audioFileType=='Podcast':
        podcast = Podcast.query.filter_by(id=audioFileID).first()
        return f'<h1>Podcast name is { podcast.name } and runtime is { podcast.duration } host {podcast.host} and participants {podcast.participants}</h1>'

    if request.method=='GET' and audioFileType=='Audiobook':
        audiobook = Audiobook.query.filter_by(id=audioFileID).first()
        return f'<h1> Audiobook title is {audiobook.title} Author is {audiobook.author} Narrator is {audiobook.narrator} Duration {audiobook.duration}</h1>'

    if request.method=='PUT' and audioFileType=='Song':
        data = request.get_json()
        song = Song.query.filter_by(id=audioFileID).first()
        if data['name']:
            song.name = data['name']
        if data['duration']:
            song.duration = data['duration']
        if data['upload_time']:
            song.upload_time = data['upload_time']
        db.session.commit()
        return '<h1>Song data updated successfully 200:OK</h1>'

    if request.method=='PUT' and audioFileType=='Podcast':
        data = request.get_json()
        podcast = Podcast.query.filter_by(id=audioFileID).first()
        if data['name']:
            podcast.name = data['name']
        if data['duration']:
            podcast.duration = data['duration']
        if data['upload_time']:
            podcast.upload_time = data['upload_time']
        if data['host']:
            podcast.host = data['host']
        if data['participants']:
            podcast.participants = data['participants']
        db.session.commit()
        return '<h1>Podcast data updated successfully 200:OK</h1>'

    if request.method=='PUT' and audioFileType=="Audiobook":
        data = request.get_json()
        audiobook = Audiobook.query.filter_by(id=audioFileID).first()
        if data['title']:
            audiobook.title = data['title']
        if data['author']:
            audiobook.author = data['author']
        if data['narrator']:
            audiobook.narrator = data['narrator']
        if data['duration']:
            audiobook.duration = data['duration']
        if data['upload_time']:
            audiobook.upload_time = data['upload_time']
        db.session.commit()
        return '<h1>Audiobook data updated successfully 200:OK</h1>'


    if request.method=='DELETE' and audioFileType=='Song':
        data = Song.query.filter_by(id=audioFileID).first()
        db.session.delete(data)
        db.session.commit()
        return '<h1>Song Data deleted successfully: 200 OK</h1>'

    if request.method=='DELETE' and audioFileType=='podcast':
        data = Podcast.query.filter_by(id=audioFileID).first()
        db.session.delete(data)
        db.session.commit()
        return '<h1>Podcast Data deleted successfully: 200 OK</h1>'

    if request.method=='DELETE' and audioFileType=='audiobook':
        data = Audiobook.query.filter_by(id=audioFileID).first()
        db.session.delete(data)
        db.session.commit()
        return '<h1>Audiobook Data deleted successfully: 200 OK</h1>'

# import requests
# put = requests.put('http://localhost:5000/Song/4', json={"name":"Human Nature", "duration":"720s"})

# put.status_code


import requests
post = requests.post('http://localhost:5000/Song', json={"name":"Cry", "duration":"450s"})

post.status_code



import requests
post = requests.post('http://localhost:5000/Audiobook/', json={'title': 'Origin', 'author':'Dan Brown', 'narrator': 'Paul Michael', 'duration': 65400})

post.status_code


import requests
post = requests.post('http://localhost:5000/Podcast/', json={'name':'On Purpose', 'duration': 1350, 'host':'Jay Shetty', 'participants': 'Kobe Bryant'})

post.status_code




# import requests
# delete = requests.delete('http://localhost:5000/Song/4')

# delete.status_code

if __name__=="__main__":
    # db.create_all()
    app.run()