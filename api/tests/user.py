import unittest
import logging
from datetime import datetime
import json
from app.models.base import *
from app.models.user import *
from app.views.user import *
from flask_json import FlaskJSON, jsonify, JsonTestResponse
from app import *

class UserTest(unittest.TestCase):

    def setUp(self):
        #create a test client of app
        self.app = app.test_client()
        #disable logs
        logging.disable(logging.CRITICAL)
        database.connect()
        database.create_tables([User], safe=True)
        # cursor = database.curser()
        # cursor.execute("CREATE TABLE User")

    def tearDown(self):
        database.drop_tables([User], safe=True)
        # cursor().execute("DROP TABLE IF EXISTS User"
        # os.close(self.app)

	# func to create user for testing purposes
	# def create_user(self, first, last, email, pwd):
	# 	# uses post to add a user to the User table
	# 	return self.app.post('/users', data=dict (
    #         first_name=first,
    #         last_name=last,
    #         email=email,
    #         password=pwd
    #     ))

    #validate if the POST request => POST /users
    def test_create(self):
		#create a user if all required parameters are sent
		# TODO TODO TODO find out what goes in bottom TODO TODO TODO

		#check the user ID
		user1 = create_user()
		self.assertEqual(user1, 1)

		#test all cases of missing parameters

		#missing first_name
		user2 = create_user()
		self.assertEqual(user2, 2)

		#missing last_name
		user3 = create_user()
		self.assertEqual(user3, 3)

		#missing email
		user4 = create_user()
		self.assertEqual(user4, 4)

		#missing password
		user5 = create_user()
		self.assertEqual(user5, 5)

		#check if an user has unique email
		unique_email_test = self.app.post('/users', data=dict(
			first_name='first_name',
			last_name='last_name',
			email='email',
			password='passwrod'
		))
		assert unique_email_test.status == 409

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
            email='email@2',
            password='password'
        ))
        #check the status code
        assert new_user.status_code == 201
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
        assert new_user.status_code == 201
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
        assert new_user.status_code == 201

        #this is the updating
        #first name
        self.app.put('/user/1', data=dict (
            frist_name='Betty'
        ))
        #check the impact of each request parameters
        list_test = self.app.get('/users/1')
        #check the status code
        assert new_user.status_code == 201

        #last name
        self.app.put('/user/1', data=dict (
            last_name='Holberton'
        ))
        list_test = self.app.get('/users/1')
        assert new_user.status_code == 201

        #email
        self.app.put('/user/1', data=dict (
            email='betty@holberton'
        ))
        list_test = self.app.get('/users/1')
        assert new_user.status_code == 201

        #password
        self.app.put('/user/1', data=dict (
            password='holbertonschool'
        ))
        list_test = self.app.get('/users/1')
        assert new_user.status_code == 201

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
