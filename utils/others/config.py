from os import getenv
from dotenv import load_dotenv


load_dotenv()


class Config(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = str(getenv('SQLALCHEMY_DATABASE_URI'))
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SECRET_KEY = str(getenv('SECRET_KEY'))
	