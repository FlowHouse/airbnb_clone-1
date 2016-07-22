import unittest
from datetime import datetime
import json
from flask_json import FlaskJSON, jsonify, JsonTestResponse
from app import *

class UserTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        db.connect()
        db.creat_tables([User], safe=True)
        # cursor = database.curser()
        # cursor.execute("CREATE TABLE User")

    def tearDown(self):
        db.drop_tables([User], safe=True)
        # cursor().execute("DROP TABLE IF EXISTS User"
        # os.close(self.app)

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


    def test_list(self):
        list_test = self.app.get('/users')
        try:
            to_dict = json.loads(list_test.data)
            return len(to_dict)
        except:
            return 0

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

        response = self.app.get('/users/2').data
        try:
            json.loads(response)
        except:
            return "user ID not linked to a user"

    # def test_delete(self):
    #
    # def test_update(self):

if __name__ == '__main__':
    unittest.main()
