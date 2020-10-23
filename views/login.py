from flask import render_template, request

from utils.app import app
from utils.others.check_password import check_sha256


@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		user_input = {
			'login': request.form.get('login'),
			'pass': request.form.get('password')
		}

	return render_template('login/index.html')
