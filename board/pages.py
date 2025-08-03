from flask import Blueprint, render_template

bp = Blueprint('pages', __name__)

@bp.route('/')
@bp.route('/login')
def login():
    return render_template('pages/login.html')

@bp.route('/sign_up')
def sign_up():
    return render_template('pages/sign_up.html')


@bp.route('/about')
def about():
    return render_template('pages/about.html')