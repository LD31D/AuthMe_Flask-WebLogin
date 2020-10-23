from flask import redirect, url_for
from flask_login import login_required, current_user

from utils.app import app


@app.route('/')
@login_required
def index():
	print(current_user)
	return ''
