from flask import redirect, url_for

from utils.app import app


@app.route('/')
def index():
	return redirect(url_for('login'))
