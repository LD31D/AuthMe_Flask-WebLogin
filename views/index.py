from flask import render_template
from flask_login import login_required, current_user

from utils.app import app


@app.route('/')
@login_required
def index():
	return render_template('index/index.html', **{'user': current_user})
