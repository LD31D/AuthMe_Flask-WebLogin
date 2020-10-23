from flask import render_template, request
from flask_login import login_user, current_user

from utils.app import app, models
from utils.others.check_password import check_sha256


@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		user_input = {
			'login': request.form.get('login'),
			'pass': request.form.get('password')
		}

		user = models.User.query.filter_by(username=user_input['login']).first()

		if user and check_sha256(user_input['pass'], user.password):
			login_user(user)

		else:
			print(False)

	return render_template('login/index.html')
