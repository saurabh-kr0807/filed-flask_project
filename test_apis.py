# -*- coding: utf-8 -*-

import unittest
import json

from app import create_app, db

class AudioServerTestCase(unittest.TestCase):
    ''' This class represents the song table test cases '''

    def setUp(self):
        '''Define test variables and initialize app.'''

        self.app = create_app()
        self.client = self.app.test_client

        # Data
        self.song = {'name': 'Smooth Criminal', 'duration': 710}
        self.podcast = {'name':'On Purpose', 'duration': 1350, 'host':'Jay Shetty', 'participants': 'Kobe Bryant'}

        self.audiobook = {'title': 'Origin', 'author':'Dan Brown', 'narrator': 'Paul Michael', 'duration': 65400}



        # binds the app to current context
        with self.app.app_context():
            # create all tables
            db.create_all()




    def test_data_insertion(self):

        '''Testing whether the api can insert a record (POST request)'''

        # Song
        # Expect the test case to pass with request status code 200
        post_song = self.client().post('/Song/', json=self.song)
        self.assertEqual(post_song.status_code, 201)

        # Podcast
        # Expect the test case to pass with request status code 200
        post_podcast = self.client().post('/Podcast/', json=self.podcast)
        self.assertEqual(post_podcast.status_code, 201)

        # Audiobook
        # Expect the test case to pass with request status code 200
        post_audiobook = self.client().post('/Audiobook/', json=self.audiobook)
        self.assertEqual(post_audiobook.status_code, 201)







    def test_get_all_data(self):
        '''Testing whether the api can fetch all the datapoints (GET request)'''


        # Song
        post_song = self.client().post('/Song/', json=self.song)
        self.assertEqual(post_song.status_code, 201)

        get_song = self.client().get('/Song/')
        song_data = get_song.json
        self.assertEqual({'name':str(song_data[0].get('name')), 'duration':str(song_data[0].get('duration'))}, {'name': 'Smooth Criminal', 'duration': '710'})

        # self.assertIn({'name': 'Smooth Criminal', 'duration': '710'}, song_data)



        # Podcast
        post_podcast = self.client().post('/Podcast/', json=self.podcast)
        self.assertEqual(post_podcast.status_code, 201)

        get_podcast = self.client().get('/Podcast/')
        podcast_data = get_podcast.json
        self.assertEqual({'name':str(podcast_data[0].get('name')), 'duration':str(podcast_data[0].get('duration')), 'host':str(podcast_data[0].get('host')), 'participants':str(podcast_data[0].get('participants'))}, {'name':'On Purpose', 'duration': '1350', 'host':'Jay Shetty', 'participants': 'Kobe Bryant'})


        # Audiobook
        post_audiobook = self.client().post('/Audiobook/', json=self.audiobook)
        self.assertEqual(post_audiobook.status_code, 201)

        get_audiobook = self.client().get('/Audiobook/')
        audiobook_data = get_audiobook.json
        self.assertEqual({'title':str(audiobook_data[0].get('title')), 'author':str(audiobook_data[0].get('author')), 'narrator':str(audiobook_data[0].get('narrator')), 'duration':str(audiobook_data[0].get('duration'))}, {'title': 'Origin', 'author':'Dan Brown', 'narrator': 'Paul Michael', 'duration': '65400'})





    def test_get_data_by_id(self):
        '''Testing whether the api can fetch data by id.'''

        # Song
        # Expect the test case to pass with request status code 200
        post_song = self.client().post('/Song/', json=self.song)
        self.assertEqual(post_song.status_code, 201)

        song_json = json.loads(post_song.data.decode('utf-8').replace("'", "\""))

        get_song = self.client().get('/Song/{}'.format(song_json['id']))
        self.assertEqual(get_song.status_code, 200)


        # Podcast
        # Expect the test case to pass with request status code 200
        post_podcast = self.client().post('/Podcast/', json=self.podcast)
        self.assertEqual(post_podcast.status_code, 201)

        podcast_json = json.loads(post_podcast.data.decode('utf-8').replace("'", "\""))
        get_podcast = self.client().get('/Podcast/{}'.format(podcast_json['id']))
        self.assertEqual(get_podcast.status_code, 200)


        # Audiobook
        # Expect the test case to pass with request status code 200
        post_audiobook = self.client().post('/Audiobook/', json=self.audiobook)
        self.assertEqual(post_audiobook.status_code, 201)

        audiobook_json = json.loads(post_audiobook.data.decode('utf-8').replace("'", "\""))
        get_audiobook = self.client().get('/Audiobook/{}'.format(audiobook_json['id']))
        self.assertEqual(get_audiobook.status_code, 200)






    def test_update_data(self):
        '''Testing whether the api can edit an existing data (PUT request).'''

        # Song
        # Expect the test case to pass with request status code 200
        post_song = self.client().post('/Song/', json=self.song)
        self.assertEqual(post_song.status_code, 201)

        put_song = self.client().put('/Song/1', json={'name':'Smooth Criminal'})
        self.assertEqual(put_song.status_code, 200)



        # Expect the test case to pass with request status code 404
        put_song = self.client().put('/Song/2', json={'name':'Smooth Criminal'})
        self.assertEqual(put_song.status_code, 404)




        # Podcast
        # Expect the test case to pass with request status code 200
        post_podcast = self.client().post('/Podcast/', json=self.podcast)
        self.assertEqual(post_podcast.status_code, 201)

        put_podcast = self.client().put('/Podcast/1', json={'name': 'impact theory', 'host': 'Tom Bilyeu', 'participants': 'Vishen Lakhiani'})
        self.assertEqual(put_podcast.status_code, 200)



        # Expect the test case to pass with request status code 404
        put_podcast = self.client().put('/Podcast/2', json={'name': 'impact theory', 'host': 'Tom Bilyeu', 'participants': 'Vishen Lakhiani'})
        self.assertEqual(put_podcast.status_code, 404)


        # Audiobook
        # Expect the test case to pass with request status code 200
        post_audiobook = self.client().post('/Audiobook/', json=self.audiobook)
        self.assertEqual(post_audiobook.status_code, 201)

        put_audiobook = self.client().put('/Audiobook/1', json={'title':'The Sandman', 'author': 'Neil Gaiman', 'narrator': 'Neil Gaiman'})
        self.assertEqual(put_audiobook.status_code, 200)



        # Expect the test case to pass with request status code 404
        put_audiobook = self.client().put('/Audiobook/2', json={'title':'The Sandman', 'author': 'Neil Gaiman', 'narrator': 'Neil Gaiman'})
        self.assertEqual(put_audiobook.status_code, 404)




    def test_delete_data(self):
        '''Testing whether the api can delete existing data (DELETE request).'''

        # Expect the test case to pass with request status code 200
        post_song = self.client().post('/Song/', json=self.song)
        self.assertEqual(post_song.status_code, 201)

        delete_song = self.client().delete('/Song/1')
        self.assertEqual(delete_song.status_code, 200)


        # Expect the test case to pass with request status code 404
        delete_song = self.client().delete('/Song/2')
        self.assertEqual(delete_song.status_code, 404)




        # Podcast
        # Expect the test case to pass with request status code 200
        post_podcast = self.client().post('/Podcast/', json= self.podcast)
        self.assertEqual(post_podcast.status_code, 201)

        delete_podcast = self.client().delete('/Podcast/1')
        self.assertEqual(delete_podcast.status_code, 200)

        # Expect the test case to pass with request status code 404
        delete_podcast = self.client().delete('/Podcast/2')
        self.assertEqual(delete_podcast.status_code, 404)


        # Audiobook
        # Expect the test case to pass with request status code 200
        post_audiobook = self.client().post('/Audiobook/', json=self.audiobook)
        self.assertEqual(post_audiobook.status_code, 201)

        delete_audiobook = self.client().delete('/Audiobook/1')
        self.assertEqual(delete_audiobook.status_code, 200)

        # Expect the test case to pass with request status code 404
        delete_audiobook = self.client().delete('/Audiobook/2')
        self.assertEqual(delete_audiobook.status_code, 404)




    def tearDown(self):
        '''teardown all initialized variables'''

        with self.app.app_context():
            # drop all tables

            db.session.remove()
            db.drop_all()



# Make the tests conveniently executable
if __name__=='__main__':
    unittest.main()
