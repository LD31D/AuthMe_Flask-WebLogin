from flask import Flask

from .others.config import Config
from .db import DataBase


app = Flask(__name__)
db = DataBase()

app.config.from_object(Config)

app.template_folder = '../templates/'
app.static_folder = '../static/'
