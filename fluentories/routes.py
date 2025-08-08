from flask import Blueprint, request, redirect, url_for, flash, render_template, session, current_app
from fluentories import db
from fluentories.forms.appointment_form import AppointmentForm
from fluentories.forms.register_form import RegisterForm
from fluentories.models import Appointment, Registeration
from fluentories.services.send_email import send_email, send_email_to_user

routes = Blueprint('core', __name__)  # Unified blueprint

# -------------------------------
# Home Page Route
# -------------------------------
@routes.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# -------------------------------
# Appointment Route
# -------------------------------
@routes.route('/appointments', methods=['GET', 'POST'])
def appointments():
    form = AppointmentForm()
    if form.validate_on_submit():
        appointment = Appointment(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            date=form.date.data,
            time= form.time.data,
            notes=form.notes.data,
            how_heard=form.how_heard.data
        )
        db.session.add(appointment)
        db.session.commit()

        # Email Body
        subject = "Appointment"
        body = f"""
👤 Name: {appointment.first_name} {appointment.last_name}

📧 Email: {appointment.email}

☎️ Phone: {appointment.phone}

📅 Date: {appointment.date.strftime('%Y-%m-%d')} at {appointment.time.strftime('%H:%M')}

📣 How They Heard About Us: {appointment.how_heard}

{"🧾 Notes:" if appointment.notes else ""}{appointment.notes if appointment.notes else 'No additional notes were provided.'}
        """
        send_email(subject, body)
        send_email_to_user(subject, appointment.email)
        flash('Appointment created successfully!', 'success')
        return redirect(url_for('core.index'))

    appointments = Appointment.query.all()
    return render_template('appointment.html', form=form, appointments=appointments)


# -------------------------------
# Registration Route
# -------------------------------
@routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        registration = Registeration(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            age=form.age.data,
            phone=form.phone.data,
            academic_level=form.academic_level.data,
            how_heard=form.how_heard.data,
            availability_time=form.availability_time.data
        )

        db.session.add(registration)
        db.session.commit()
        subject = "Registration"
        body = f"""
👤 Name: {registration.first_name} {registration.last_name}

📧 Email: {registration.email}

🎂 Age: {registration.age}

☎️ Phone: {registration.phone}

🎓 Academic Level: {registration.academic_level}

📣 How They Heard About Us: {registration.how_heard}

🕒 Available on {registration.availability_time}
        """
        send_email(subject, body)
        send_email_to_user(subject, registration.email)

        flash('Registration successful!', 'success')
        return redirect(url_for('core.index'))

    registrations = Registeration.query.all()
    return render_template('register.html', form=form, registrations=registrations)

@routes.route('/change_lang/<lang_code>')
def change_lang(lang_code):
    if lang_code in current_app.config['BABEL_SUPPORTED_LOCALES']:
        session['lang'] = lang_code
    return redirect(request.referrer or url_for('core.index'))    