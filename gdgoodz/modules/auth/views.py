from flask import Blueprint, request, render_template, redirect, url_for
from .controller import AuthController

bp = Blueprint('auth', __name__)
controller = AuthController()


@bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    ''' Registers a new user account '''

    if request.method == 'POST':
        reg_form = request.form
        valid, errors = controller.register_new_user(reg_form)

        if valid is True and errors is None:
            return redirect(url_for('auth.login'))
        else:
            return render_template('auth/register.html', title='GDgoodZ Trading - Registration', errors=errors)

    return render_template('auth/register.html', title='GDgoodZ Trading - Registration')


@bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    ''' Logs a user into their account '''

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        errors = controller.login_user(username, password)

        if errors is not None:
            return render_template('auth/login.html', title='GDgoodZ Trading - Login', errors=errors)
        else:
            return redirect(url_for('index'))

    if request.args.get('login_required_error'):
        return render_template('auth/login.html', title='GDgoodZ Trading - Login', errors=[request.args.get('login_required_error')])
    else:
        return render_template('auth/login.html', title='GDgoodZ Trading - Login')


@bp.route('/auth/login_required')
def login_required():
    return redirect(url_for('auth.login', login_required_error='You must be logged in to view the requested page!'))


@bp.route('/auth/logout')
def logout():
    controller.clear_user_session()
    
    return redirect(url_for('auth.login'))