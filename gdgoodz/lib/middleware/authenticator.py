from flask import session, redirect, url_for
from functools import wraps

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'uid' not in session and 'username' not in session:
            return redirect(url_for('auth.login_required'))
        return f(*args, **kwargs)
    return wrapper