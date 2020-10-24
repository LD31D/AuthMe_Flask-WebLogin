from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user

from utils.app import app, models
from utils.others.check_password import check_sha256


@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		login = request.form.get('login').strip().lower()
		trypass = request.form.get('password')

		if login and trypass:
			user = models.User.query.filter_by(username=login).first()

			if user and check_sha256(trypass, user.password):
				login_user(user)

				next_page = request.args.get('next')

				if next_page:
					return redirect(next_page)

				else:
					return redirect(url_for('index'))

			else:
				flash('Invalid login or password')

		else:
			flash('Fields shouldn\'t be empty')

	return render_template('login/index.html')
