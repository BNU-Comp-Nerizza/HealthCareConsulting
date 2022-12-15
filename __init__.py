from flask_login import login_required
from flask_login import LoginManager
from flask import *

import application as main_file

application = main_file.application

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('userlogin'))

    return wrap