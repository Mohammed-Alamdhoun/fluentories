from fluentories import db

class Appointment(db.Model):
    """Model for storing appointment details."""
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    date = db.Column(db.Date, nullable=False)
    how_heard = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    
    def __init__(self, first_name, last_name, email, phone, date, how_heard, notes=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.date = date
        self.how_heard = how_heard
        self.notes = notes

    def __repr__(self):
        return f'<Appointment {self.id} on {self.date} for {self.first_name} {self.last_name}>'
    
class Registeration(db.Model):
    """Model for storing registration details."""
    __tablename__ = 'registrations'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    academic_level = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    how_heard = db.Column(db.String(50), nullable=False)
    availability_time = db.Column(db.Date, nullable=False)
    
    def __init__(self, first_name, last_name, email, age, phone, academic_level, date_of_birth, how_heard, availability_time):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.phone = phone
        self.academic_level = academic_level
        self.date_of_birth = date_of_birth
        self.how_heard = how_heard
        self.availability_time = availability_time

    def __repr__(self):
        return f'<Registration {self.id} for {self.first_name} {self.last_name}>'