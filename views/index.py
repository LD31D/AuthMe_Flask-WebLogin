from flask import redirect, url_for
from flask_login import login_required, current_user

from utils.app import app


@login_required
@app.route('/')
def index():
	print(current_user)
	return ''
