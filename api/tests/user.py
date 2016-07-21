<<<<<<< HEAD
import unittest
=======
# test github pull from head to forked repo
import unittest
# import logging
>>>>>>> d60654afca5bdc3341aa728629eb31809c49d75b
from datetime import datetime
import json
from flask_json import FlaskJSON, jsonify, JsonTestResponse
from app import *

class UserTest(unittest.TestCase):
<<<<<<< HEAD

    def setUp(self):
        self.app = app.test_client()
        app.response_class = JsonTestResponse
        connection.cursor().execute("CREATE TABLE User")
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        os.close(self.app)
        connection.cursor().execute("DROP TABLE User")

    def test_create(self):

    def test_list(self):

    def test_get(self):

    def test_delete(self):

    def test_update(self):

if __name__ == '__main__':
    unittest.main()
=======
	"""docstring for BaseTest"""
	#response = requests.get('http://127.0.0.1:5555/')

	# to create a test client of app
	def setUp(self):
		self.app = app.test_client()
		app.response_class = JsonTestResponse
		logging.disable(logging.CRITICAL)

	# to drop User table
	def tearDown(self):
		pass

	# validate te POST request of Users
	def test_create(self):
		data = request.form
		email_check = User.select().where(User.email == data['email'])
		if email_check:
		return {'code': 10000, 'msg': 'Email already exists'}, 409

		user = User(
			email = data['email'],
			first_name = data['first_name'],
			last_name = data['last_name']
		)
		user.set_password(data['password'])
		user.save()

		return {'code': 201,'msg': 'User was created successfully'}, 201


if __name__ == '__main__':
	unittest.main()
>>>>>>> d60654afca5bdc3341aa728629eb31809c49d75b
