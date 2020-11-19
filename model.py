"""Models for Sleep Journal app"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user on the site"""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User user_id={self.user_id} full_name={self.full_name} email={self.email}>'


class User_entry(db.Model):
    """A user entry on the site"""
    __tablename__ = 'user_entries'

    user_entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    sleeptime = db.Column(db.DateTime)
    waketime = db.Column(db.DateTime)
    sleep_quality = db.Column(db.Integer, nullable=False)
    stress_level = db.Column(db.Integer)
    energy_level = db.Column(db.Integer)
    productivity_level = db.Column(db.Integer)
    exercise_level = db.Column(db.Integer)
    alcoholic_units = db.Column(db.String)
    user = db.relationship('User')

    def __repr__(self):
        return f'<User_entry user_entry_id={self.user_entry_id} sleeptime={self.sleeptime} waketime={self.waketime} sleep_quality={self.sleep_quality}>'
    

class Mood(db.Model):
    """List of moods to choose from"""
    __tablename__ = 'moods'

    mood_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    mood = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Mood mood_id={self.mood_id} mood={self.mood}>'


class User_entry_mood(db.Model):
    """Moods that user chooses"""
    __tablename__ = 'user_entry_moods'

    user_entry_mood_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_entry_id = db.Column(db.Integer, db.ForeignKey('user_entries.user_entry_id'), nullable=False)
    mood_id = db.Column(db.Integer, db.ForeignKey('moods.mood_id'), nullable=False)
    
    user_entry = db.relationship('User_entry')
    mood = db.relationship('Mood')

    def __repr__(self):
        return f'<User_entry_mood user_entry_mood_id={self.user_entry_mood_id} mood_id={self.mood_id}>'


class Medication(db.Model):
    """List of medications to choose from"""
    __tablename__ = 'medications'

    medication_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    medication = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Medication medication_id={self.medication_id} medication={self.medication}>'


class User_entry_medication(db.Model):
    """Medications that user chooses"""
    __tablename__ = 'user_entry_medications'

    user_entry_medication_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_entry_id = db.Column(db.Integer, db.ForeignKey('user_entries.user_entry_id'), nullable=False)
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.medication_id'), nullable=False)
    
    user_entry = db.relationship('User_entry')
    medication = db.relationship('Medication')

    def __repr__(self):
        return f'<User_entry_medication user_entry_medication_id={self.user_entry_medication_id} medication_id={self.medication_id}>'


class Symptom(db.Model):
    """List of symptoms to choose from"""
    __tablename__ = 'symptoms'

    symptom_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    symptom = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Symptom symptom_id={self.symptom_id} symptom={self.symptom}>'


class User_entry_symptom(db.Model):
    """Symptoms that user chooses"""
    __tablename__ = 'user_entry_symptoms'

    user_entry_symptom_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_entry_id = db.Column(db.Integer, db.ForeignKey('user_entries.user_entry_id'), nullable=False)
    symptom_id = db.Column(db.Integer, db.ForeignKey('symptoms.symptom_id'), nullable=False)
    
    user_entry = db.relationship('User_entry')
    symptom = db.relationship('Symptom')

    def __repr__(self):
        return f'<User_entry_symptom user_entry_symptom_id={self.user_entry_symptom_id} symptom_id={self.symptom_id}>'


def connect_to_db(flask_app, db_uri='postgresql:///sleepjournal', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
