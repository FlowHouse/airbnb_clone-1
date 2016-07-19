# test github pull from head to forked repo
import unittest
from datetime import datetime
import json
from flask_json import FlaskJSON, jsonify, JsonTestResponse
from app import *

class BaseTest(unittest.TestCase):
	"""docstring for BaseTest"""
	#response = requests.get('http://127.0.0.1:5555/')

	# to create a test client of app
	def setUp(self):
		self.app = app.test_client()
        app.response_class = JsonTestResponse

	# to validate if status of the JSON resp of GET / is equal to 200
	def test_200(self):
		response = self.app.get('/')
		assert response.status_code == 200

	# to validate if status of the JSON resp of GET / is equal to OK
	def test_status(self):
		response = self.app.get('/')
		# print response
		# json_r = json.dumps(response)
		# data = json.loads(response)
		# print data
		assert response.json['status'] == 'OK'

	# to validate if time of the JSON resp of GET / is equal of local time
	def test_time(self):
		response = self.app.get('/')
		dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		# data = json.loads(response.data)
		assert response.json['time'] == dt

	# to validate if utc time of the JSON resp of GET / is equal of utc time
	def test_time_utc(self):
		response = self.app.get('/')
		dt = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
		# data = json.loads(response.data)
		assert response.json['utc_time'] == dt

if __name__ == '__main__':
	unittest.main()
