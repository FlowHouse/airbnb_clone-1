"""
 ===----Task 2------------------------------------------------------------------------===
	Airbnb Clone Project, Task 2.
	Isolating environments in Python: Development/Production.
 ===----------------------------------------------------------------------------------===
"""
import os
from peewee import *

ENV = os.environ
if 'AIRBNB_ENV' not in ENV:
    raise Exception("Environment variable AIRBNB_ENV not set")

test = True if ENV['AIRBNB_ENV'] == 'production' else False

DEBUG = (True, False)[test]
HOST = ('localhost', '0.0.0.0')[test]
PORT = (3333, 3000)[test]
DATABASE = {
    'host': '158.69.78.253',
    'user': ( 'airbnb_user_dev', 'airbnb_user_prod')[test],
    'database': ('airbnb_dev', 'airbnb_prod')[test],
    'port': '3306',
    'charset': 'utf8',
    'password': (ENV.get('AIRBNB_DATABASE_PWD_DEV'), ENV.get('AIRBNB_DATABASE_PWD_PROD'))[test]
}