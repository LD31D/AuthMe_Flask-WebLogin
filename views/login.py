from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required

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

			next_page = request.args.get('next')

			if next_page:
				return redirect(next_page)

			else:
				return redirect(url_for('index'))

		else:
			print(False)

	return render_template('login/index.html')


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login') + '?next=' + request.url)

    return response


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
