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
    
@bp.route('/gallery')
def gallery():
    return render_template('pages/gallery.html')

@bp.route('/booking')
def booking():
    return render_template('pages/booking.html')

@bp.route('/clients')
def clients():
    clients = [
        {
            "name": "Vivaan Gupta",
            "phone":"0400 123 456",
            "num_visits": 5,
            "service_type": "Fade",
            "last_visit": "2025-08-01"
        },
        {
            "name": "Suddy Hosur",
            "phone":"0400 123 456",
            "num_visits": 5,
            "service_type": "Fade",
            "last_visit": "2025-08-01"
        },
        {
            "name": "Suddy Hosur",
            "phone":"0400 123 456",
            "num_visits": 5,
            "service_type": "Fade",
            "last_visit": "2025-08-01"
        },
        {
            "name": "Suddy Hosur",
            "phone":"0400 123 456",
            "num_visits": 5,
            "service_type": "Fade",
            "last_visit": "2025-08-01"
        }
    ]

    return render_template('pages/clients.html', clients=clients)

@bp.route('/timetable')
def timetable():
    return render_template('pages/timetable.html')

@bp.route('/finance_report')
def finance_report():
    return render_template('pages/finance_report.html')

