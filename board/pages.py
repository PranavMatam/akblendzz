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
    time_slots = [
        "4:00 - 4:30", "4:30 - 5:00", "5:00 - 5:30", 
        "5:30 - 6:00", "6:00 - 6:30", "6:30 - 7:00", 
        "7:00 - 7:30"
    ]

    schedule = {
        "Monday": {
            "4:00 - 4:30": {"status": "requested", "clients": ["Client 1", "Client 2", "Client 3"]},
            "4:30 - 5:00": {"status": "requested", "clients": ["Client 4"]},
            "5:00 - 5:30": {"status": "available"},
            "6:30 - 7:00": {"status": "booked"},
            "7:00 - 7:30": {"status": "booked"},
        },
        # You can add other days similarly
    }

    # Set all empty cells to "available"
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        schedule.setdefault(day, {})
        for slot in time_slots:
            schedule[day].setdefault(slot, {"status": "available"})

    return render_template("pages/timetable.html", time_slots=time_slots, schedule=schedule)


@bp.route('/finance_report')
def finance_report():
    days = [
        {"name": "Monday", "appointments": 5, "revenue": 150},
        {"name": "Tuesday", "appointments": 3, "revenue": 90},
        # ...
    ]
    services = [
        {"name": "Fade", "bookings": 10, "revenue": 300},
        {"name": "Beard", "bookings": 5, "revenue": 150},
        {"name": "Fade + Beard", "bookings": 3, "revenue": 120},
    ]
    return render_template("pages/finance_report.html", days=days, services=services)


