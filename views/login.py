from flask import render_template

from utils.app import app


@app.route('/login/', methods=['GET', 'POST'])
def login():
	return render_template('login/index.html')
