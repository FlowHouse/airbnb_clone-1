import unittest
from datetime import datetime
import json
from flask_json import FlaskJSON, jsonify, JsonTestResponse
from app import *

class UserTest(unittest.TestCase):

    def setUp(self):
        #create a test client of app
        self.app = app.test_client()
        #disable logs
        logging.disable(logging.CRITICAL)
        #create User table
        db.connect()
        db.creat_tables([User], safe=True)

        # cursor = database.curser()
        # cursor.execute("CREATE TABLE User")

    def tearDown(self):
        #drop User table
        db.drop_tables([User], safe=True)
        # cursor().execute("DROP TABLE IF EXISTS User"
        # os.close(self.app)

        #validate if the POST request => POST /users
    def test_create(self):
        #create a user if all required parameters are sent
        self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email='eamil@1',
            password='password'
        ))
        #check the user ID
        set.assertEqual(User.select(id), 1)

        #test all cases of missing parameters

        #missing first_name
        self.app.post('/users', data=dict (
            first_name=' ',
            last_name='last_name',
            email='email@2',
            password='password'
        ))
        set.assertEqual(User.select(id), 2)

        #missing last_name
        self.app.post('/users', data=dict (
            first_name='first_name',
            last_name=' ',
            email='email@3',
            password='password'
        ))
        set.assertEqual(User.select(id), 3)

        #missing email
        self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email=' ',
            password='password'
        ))
        set.assertEqual(User.select(id), 4)

        #missing password
        self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email='email@5',
            password=' '
        ))
        set.assertEqual(User.select(id), 5)

        #TODO
        #check if an user has unique email

    #validate if the GET request => GET /users:
    def test_list(self):
        list_test = self.app.get('/users')
        try:
            to_dict = json.loads(list_test.data)
            #return 1 element after a user creation
            return len(to_dict)
        except:
            #return 0 elements if no user was created
            return 0

    #validate if the GET request on a user ID => GET /users/<user_id>:
    def test_get(self):
        #create a user and after get it
        new_user = self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email='email@1',
            password='password'
        ))
        #check the status code
        assert new_user.status_code == 200
        #this is the getting
        response = self.app.get('/users/1').data
        #check if it's the same resource as during the creation
        assert sorted(response) == sorted(new_user.data)

        #check when trying to get an unknown user
        #try unknown user
        response = self.app.get('/users/2').data
        try:
            json.loads(response)
        except:
            return "user ID not linked to a user"

    #validate if the DELETE request on a user ID => DELETE /users/<user_id>:
    def test_delete(self):
        #create a user and after delete it
        new_user = self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email='email@1',
            password='password'
        ))
        #check the status code
        assert new_user.status_code == 200
        list_test = self.app.get('/users')
        to_dict = json.loadds(list_test.data)
        #check the number of element before and after a delete
        assert len(to_dict) == 1
        #this is the deleting
        self.app.delete('/users/1')
        #check when trying to delete an unknown user
        response = self.app.get('/users/2').data
        try:
            json.loads(response)
        except:
            return "user ID not linked to a user"

    #validate if the PUT request on a user ID => PUT /users/<user_id>:
    def test_update(self):
        #create a user and after update it
        new_user = self.app.post('/users', data=dict (
            first_name='first_name',
            last_name='last_name',
            email='email@1',
            password='password'
        ))
        assert new_user.status_code == 200

        #this is the updating
        #first name
        self.app.put('/user/1', data=dict (
            frist_name='Betty'
        ))
        #check the impact of each request parameters
        list_test = self.app.get('/users/1')
        #check the status code
        assert new_user.status_code == 200

        #last name
        self.app.put('/user/1', data=dict (
            last_name='Holberton'
        ))
        list_test = self.app.get('/users/1')
        assert new_user.status_code == 200

        #email
        self.app.put('/user/1', data=dict (
            email='betty@holberton'
        ))
        list_test = self.app.get('/users/1')
        assert new_user.status_code == 200

        #password
        self.app.put('/user/1', data=dict (
            password='holbertonschool'
        ))
        list_test = self.app.get('/users/1')
        assert new_user.status_code == 200

        #check when trying to update an unknown user
        #try unknown user
        self.app.put('/users/2', data=dict(
            first_name="first_name"
        ))
        response = self.app.get('/users/2').data
        try:
            json.loads(response)
        except:
            return "user ID not linked to a user"


if __name__ == '__main__':
    unittest.main()
