from flask import redirect, url_for
from flask_login import logout_user, login_required

from utils.app import app


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
