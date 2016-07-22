import unittest
import logging
from datetime import datetime
import json
from app.models.base import *
from flask_json import FlaskJSON, jsonify, JsonTestResponse
from app import *

class UserTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        database.connect()
        database.create_tables([User], safe=True)
        # cursor = database.curser()
        # cursor.execute("CREATE TABLE User")

    def tearDown(self):
        database.drop_tables([User], safe=True)
        # cursor().execute("DROP TABLE IF EXISTS User"
        # os.close(self.app)

        #validate if the POST request => POST /users
    def test_create(self):
        self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email='eamil@1',
            password='password'
        ))
        set.assertEqual(User.select(id), 1)

        self.app.post('/users', data=dict (
            first_name=' ',
            last_name='last_name',
            email='email@2',
            password='password'
        ))
        set.assertEqual(User.select(id), 2)

        self.app.post('/users', data=dict (
            first_name='first_name',
            last_name=' ',
            email='email@3',
            password='password'
        ))
        set.assertEqual(User.select(id), 3)

        self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email=' ',
            password='password'
        ))
        set.assertEqual(User.select(id), 4)

        self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email='email@5',
            password=' '
        ))
        set.assertEqual(User.select(id), 5)

    #validate if the GET request => GET /users:
    def test_list(self):
        list_test = self.app.get('/users')
        try:
            to_dict = json.loads(list_test.data)
            return len(to_dict)
        except:
            return 0

    #validate if the GET request on a user ID => GET /users/<user_id>:
    def test_get(self):
        new_user = self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email='email@1',
            password='password'
        ))
        assert new_user.status_code == 200
        response = self.app.get('/users/1').data
        assert sorted(response) == sorted(new_user.data)

        #try unknown user
        response = self.app.get('/users/2').data
        try:
            json.loads(response)
        except:
            return "user ID not linked to a user"

    #validate if the DELETE request on a user ID => DELETE /users/<user_id>:
    def test_delete(self):
        new_user = self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email='email@1',
            password='password'
        ))
        list_test = self.app.get('/users')
        to_dict = json.loadds(list_test.data)
        assert len(to_dict) == 1
        self.app.delete('/users/1')

    #validate if the PUT request on a user ID => PUT /users/<user_id>:
    # def test_update(self):

if __name__ == '__main__':
    unittest.main()
