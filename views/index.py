from flask import redirect, url_for
from flask_login import current_user

from utils.app import app


@app.route('/')
def index():
	print(current_user)
	return redirect(url_for('login'))
