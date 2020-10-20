from flask import (
	Flask, 
	render_template, 
	redirect, 
	url_for
	)

app = Flask(__name__)


@app.route('/')
def index():
	return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
	return render_template('login/index.html')


if __name__ == '__main__':
	app.run(debug=True)
