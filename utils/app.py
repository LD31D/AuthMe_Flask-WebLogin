from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .others.config import Config


app = Flask(__name__)

app.config.from_object(Config)

app.template_folder = '../templates/'
app.static_folder = '../static/'

db = SQLAlchemy(app)
manager = LoginManager(app)

db.Model.metadata.reflect(db.engine)

from .db import models

