from flask import redirect, url_for, request

from utils.app import app


@app.after_request
def redirect_to_login_page(response):
    if response.status_code == 401:
        return redirect(url_for('login') + '?next=' + request.url)

    elif response.status_code == 404:
    	return redirect(url_for('index'))

    return response
