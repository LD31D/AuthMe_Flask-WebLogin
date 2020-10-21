from flask import Flask

from .others.config import Config


app = Flask(__name__)

app.config.from_object(Config)

app.template_folder = '../templates/'
app.static_folder = '../static/'
