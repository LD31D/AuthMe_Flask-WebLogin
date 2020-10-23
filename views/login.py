from flask import render_template, request

from utils.app import app, db
from utils.others.check_password import check_sha256


@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		user_input = {
			'login': request.form.get('login'),
			'pass': request.form.get('password')
		}

		# user = db.select_user_for_name(user_input['login'])

		# if user and check_sha256(user_input['pass'], user[3]):
		# 	print(True)

		# else:
		# 	print(False)

	return render_template('login/index.html')
