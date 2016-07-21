# test github pull from head to forked repo
import unittest
# import logging
from datetime import datetime
import json
from flask_json import FlaskJSON, jsonify, JsonTestResponse
from app import *

class UserTest(unittest.TestCase):
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
