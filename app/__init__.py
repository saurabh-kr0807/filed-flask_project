
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, marshal_with
from datetime import datetime
import json

# Initialize sql-alchemy
db = SQLAlchemy()

song_update_args = reqparse.RequestParser()
song_update_args.add_argument("name", type=str, help="Name of the song required")
song_update_args.add_argument("duration", type=int, help="Duration of the song")
song_update_args.add_argument("upload_time", type=datetime, help="time is required of the songs")

audiobook_update_args = reqparse.RequestParser()
audiobook_update_args.add_argument("title", type=str, help="title of the audiobook required")
audiobook_update_args.add_argument("author", type=str, help="Author name required" )
audiobook_update_args.add_argument("narrator", type=str, help="Narrator name required")
audiobook_update_args.add_argument("duration", type=int, help="Dureation of the audiobook required")
audiobook_update_args.add_argument("upload_time", type=datetime, help="time is required of the audiobook")

podcast_update_args = reqparse.RequestParser()
podcast_update_args.add_argument("name", type=str, help="Name of the Podcast required")
podcast_update_args.add_argument("duration", type=int, help="Dureation of the Podcast required")
podcast_update_args.add_argument("upload_time", type=datetime, help="time is required of the Podcast")
podcast_update_args.add_argument("host", type=str, help="Host of the Podcast required")
podcast_update_args.add_argument("participants", type=str, help="participants of the Podcast required")


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)


    # app = create_app()

    from app.models import Song, Podcast, Audiobook

    @app.route('/', methods=['GET'])
    def server_status():
        response = {'Server': 'Running'}
        # response.status_code = 200

        return (
            json.dumps(response, default=str),
            200,
            {'Content-Type': "application/json"}
            )



    @app.route('/<audioFileType>/', methods=['GET','POST'])
    def get_insert_data(audioFileType):


        if request.method=='GET':
            # GET all the Songs table information from this get method using Api
            if audioFileType=='Song':
                songs = Song.query.all()
                results = []

                for song in songs:
                    _object = {
                        'id': song.id,
                        'name': song.name,
                        'duration': song.duration,
                        'upload_time': song.upload_time
                        }
                    results.append(_object)

                # response = jsonify(results)
                # response.status_code = 200
                return (
                    json.dumps(results, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )
            # GET all the Podcast table information from this get method using Api
            if audioFileType=='Podcast':
                podcasts = Podcast.query.all()
                results = []

                for podcast in podcasts:
                    _object = {
                        'id': podcast.id,
                        'name': podcast.name,
                        'duration': podcast.duration,
                        'upload_time': podcast.upload_time,
                        'host': podcast.host,
                        'participants': podcast.participants
                        }
                    results.append(_object)

                # response = jsonify(results)
                # response.status_code = 200
                return (
                    json.dumps(results, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )

            # GET all the Audiobook table information from this get method using Api
            if audioFileType=='Audiobook':
                audiobooks = Audiobook.query.all()
                results = []

                for audiobook in audiobooks:
                    _object = {
                        'id': audiobook.id,
                        'title': audiobook.title,
                        'author': audiobook.author,
                        'narrator': audiobook.narrator,
                        'duration': audiobook.duration,
                        'upload_time': audiobook.upload_time
                        }
                    results.append(_object)

                # response = jsonify(results)
                # response.status_code = 200
                return (
                    json.dumps(results, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )


        if request.method=='POST':
            # POST the data Songs table  from this post method using Api
            if audioFileType=='Song':
                data = request.json
                # name = data['name']
                name = str(data.get('name'))
                # duration = data['duration']
                duration = str(data.get('duration'))
                # upload_time = data['upload_time']

                song = Song(name=name, duration=duration)

                db.session.add(song)
                db.session.commit()

                response = {
                    'id': song.id,
                    'name': song.name,
                    'duration': song.duration,
                    'upload_time': song.upload_time
                    }
                # response.status_code = 201

                return (
                    json.dumps(response, default=str),
                    201,
                    {'Content-Type': "application/json"}
                    )

            # POST the data Podcast table  from this post method using Api
            if audioFileType=='Podcast':
                data = request.json
                name = str(data.get('name'))
                duration = str(data.get('duration'))
                host = str(data.get('host'))
                participants = str(data.get('participants'))

                podcast = Podcast(name=name, duration=duration, host=host, participants=participants)

                db.session.add(podcast)
                db.session.commit()

                response = {
                    'id': podcast.id,
                    'name': podcast.name,
                    'duration': podcast.duration,
                    'upload_time': podcast.upload_time,
                    'host': podcast.host,
                    'participants': podcast.participants
                    }
                # response.status_code = 201

                return (
                    json.dumps(response, default=str),
                    201,
                    {'Content-Type': "application/json"}
                    )

            # POST the data Audiobook table  from this post method using Api
            if audioFileType=='Audiobook':
                data = request.json
                title = str(data.get('title'))
                author = str(data.get('author'))
                narrator = str(data.get('narrator'))
                duration = str(data.get('duration'))

                audiobook = Audiobook(title=title, author=author, narrator=narrator, duration=duration)

                db.session.add(audiobook)
                db.session.commit()

                response = {
                    'id': audiobook.id,
                    'title': audiobook.title,
                    'author': audiobook.author,
                    'narrator': audiobook.narrator,
                    'duration': audiobook.duration,
                    'upload_time': audiobook.upload_time
                    }
                # response.status_code = 201

                return (
                    json.dumps(response, default=str),
                    201,
                    {'Content-Type': "application/json"}
                    )


    @app.route('/<audioFileType>/<audioFileID>', methods=['GET','PUT','DELETE'])
    def get_update_delete_data(audioFileType, audioFileID):


        # Get method for get the Song information from Api call using song_id filter
        if request.method=='GET' and audioFileType=='Song':
            song = Song.query.filter_by(id=audioFileID).first()
            if not song:
                response = {"message":"Song id not found"}

                return (
                    json.dumps(response),
                    404,
                    {'Content-Type': "application/json"}
                    )
            response = {
                'id': song.id,
                'name': song.name,
                'duration': song.duration,
                'upload_time': song.upload_time
                }
            # response.status_code = 200

            return (
                    json.dumps(response, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )


        # Get method for get the Podcast information from Api call using podcast_id filter
        if request.method=='GET' and audioFileType=='Podcast':
            podcast = Podcast.query.filter_by(id=audioFileID).first()
            if not podcast:
                message = {"message":"Podcast id not found"}

                return (
                    json.dumps(message, default=str),
                    404,
                    {'Content-Type': "application/json"}
                    )

            response = {
                'id': podcast.id,
                'name': podcast.name,
                'duration': podcast.duration,
                'upload_time': podcast.upload_time,
                'host': podcast.host,
                'participants': podcast.participants
                }
            # response.status_code = 200

            return (
                    json.dumps(response, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )


        # Get method for get the Audiobook information from Api call using audiobook_id filter
        if request.method=='GET' and audioFileType=='Audiobook':
            audiobook = Audiobook.query.filter_by(id=audioFileID).first()
            if not audiobook:
                message = {"message":"Audiobook id not found"}

                return (
                    json.dumps(message, default=str),
                    404,
                    {'Content-Type': "application/json"}
                    )

            response = {
                'id': audiobook.id,
                'title': audiobook.title,
                'author': audiobook.author,
                'narrator': audiobook.narrator,
                'duration': audiobook.duration,
                'upload_time': audiobook.upload_time
                }
            # response.status_code = 200

            return (
                    json.dumps(response, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )

        # PUT method for updating the data in the Song table filter by song_id
        if request.method=='PUT' and audioFileType=='Song':
            data = song_update_args.parse_args()
            # data = request.json
            song = Song.query.filter_by(id=audioFileID).first()
            if not song:
                message = {"message":"Song id not found"}

                return (
                    json.dumps(message, default=str),
                    404,
                    {'Content-Type': "application/json"}
                    )
            if data['name']:
                song.name = data['name']
            if data['duration']:
                song.duration = data['duration']
            if data['upload_time']:
                song.upload_time = data['upload_time']
            db.session.commit()
            response = {
                'name': song.name,
                'duration': song.duration
                }
            # response.status_code = 200
            return (
                    json.dumps(response, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )

        # PUT method for updating the data in the Podcast table filter by podcast_id
        if request.method=='PUT' and audioFileType=='Podcast':
            data = podcast_update_args.parse_args()
            podcast = Podcast.query.filter_by(id=audioFileID).first()
            if not podcast:
                message = {"message":"Podcast id not found"}
                return (
                    json.dumps(message, default=str),
                    404,
                    {'Content-Type': "application/json"}
                    )
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
            response = {
                'id': podcast.id,
                'name': podcast.name,
                'duration': podcast.duration,
                'upload_time': podcast.upload_time,
                'host': podcast.host,
                'participants': podcast.participants
                }
            # response.status_code = 200
            return (
                    json.dumps(response, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )

        # PUT method for updating the data in the Audiobook table filter by audiobook_id
        if request.method=='PUT' and audioFileType=="Audiobook":
            data = audiobook_update_args.parse_args()
            audiobook = Audiobook.query.filter_by(id=audioFileID).first()
            if not audiobook:
                message = {"message":"Audiobook id not found"}
                return (
                    json.dumps(message, default=str),
                    404,
                    {'Content-Type': "application/json"}
                    )
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
            response = {
                'id': audiobook.id,
                'title': audiobook.title,
                'author': audiobook.author,
                'narrator': audiobook.narrator,
                'duration': audiobook.duration,
                'upload_time': audiobook.upload_time
                }
            # response.status_code = 200
            return (
                    json.dumps(response, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )


        # DELETE method for delete the Song information from Api call using song_id filter
        if request.method=='DELETE' and audioFileType=='Song':
            data = Song.query.filter_by(id=audioFileID).first()
            if not data:
                message = {"message":"Song id not found"}

                return (
                    json.dumps(message, default=str),
                    404,
                    {'Content-Type': "application/json"}
                    )
            db.session.delete(data)
            db.session.commit()

            message = {"message": "song {} deleted successfully".format(audioFileID)}
            return (
                    json.dumps(message, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )

        # Delete method for delete the Podcast information from Api call using podcast_id filter
        if request.method=='DELETE' and audioFileType=='Podcast':
            data = Podcast.query.filter_by(id=audioFileID).first()
            if not data:
                message = {"message":"Podcast id not found"}
                return (
                    json.dumps(message, default=str),
                    404,
                    {'Content-Type': "application/json"}
                    )
            db.session.delete(data)
            db.session.commit()

            message = {"message": "podcast {} deleted successfully".format(audioFileID)}
            return (
                    json.dumps(message, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )


        # Delete method for delete the Audiobook information from Api call using audiobook_id filter
        if request.method=='DELETE' and audioFileType=='Audiobook':
            data = Audiobook.query.filter_by(id=audioFileID).first()
            if not data:
                message = {"message":"Audiobook id not found"}
                return (
                    json.dumps(message, default=str),
                    404,
                    {'Content-Type': "application/json"}
                    )

            db.session.delete(data)
            db.session.commit()

            message = {"message": "Audiobook {} deleted successfully".format(audioFileID)}
            return (
                    json.dumps(message, default=str),
                    200,
                    {'Content-Type': "application/json"}
                    )


    return app
