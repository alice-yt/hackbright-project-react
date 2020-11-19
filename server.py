"""Server for Sleep Journal app"""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import db, User, User_entry, Mood, User_entry_mood, Medication, User_entry_medication, Symptom, User_entry_symptom, connect_to_db 
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View login page"""

    return render_template('homepage.html')


@app.route('/create_account')
def create_account():
    """View account creation page"""

    return render_template('create_account.html')


@app.route('/menu')
def menu():
    """View menu page"""
    print('reached menu')

    return render_template('menu.html')


@app.route('/time_entry')
def log_sleeptimes():
    """Log sleep and wake time"""

    return render_template('time_entry.html')


@app.route('/journal_entry')
def log_entry():
    """Log entry"""

    return render_template('journal_entry.html')


# experimenting with combining two pages of forms into one
@app.route('/log_entry')
def log_combined_entry():
    """Log entry"""

    return render_template('combined_form.html')


@app.route('/user_entries')
def all_user_entries():
    """View all user entries of user within the session"""
    # query that filters for entry for user in your session

    if 'user' in session:
        user = session['user']

    user = crud.get_user_by_id(session['user'])
    user_entries = crud.get_use_entry_by_id(user_entry_id)

    return render_template('all_user_entries.html', user_entries=user_entries)

    # user_entry = crud.create_user_entry(user.user_id, sleeptime, waketime, sleep_quality, stress_level, energy_level, productivity_level, exercise_level, alcoholic_units)

    # user_entries = crud.get_user_entries()

    # return render_template('all_user_entries.html', user_entries=user_entries)


# check what this is doing
@app.route('/user_entries/<user_entry_id>') 
def show_user_entry(user_entry_id):
    """Show user entry details"""

    user_entry = crud.get_user_by_email(email)

    return render_template('user_entry_details.html', user_entry=user_entry)


@app.route('/sleep_insights')
def view_sleep_analysis():
    """View charts and analysis of sleep"""

    return render_template('sleep_insights.html')


@app.route('/users')
def all_users():

    users = crud.get_users()

    return render_template('all_users.html', users=users)  


# check what this is doing
@app.route('/users/<user_id>')
def show_user(user_id):
    """Show user details"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


@app.route('/create_account', methods=['POST'])
def register_user():
    """Create User"""

    full_name = request.form.get('full-name')
    email = request.form.get('create-email')
    password = request.form.get('create-password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Please try again.') 

    else:
        crud.create_user(full_name, email, password)
        flash('Account created! Please log in.')
    
    return redirect('/')


@app.route('/', methods=['POST'])
def login_user():
    """Login User"""
    print('LOGIN')
    email = request.form.get('login-email')
    password = request.form.get('login-password')

    user = crud.get_user_by_email(email)
    print('USER')
    if user.password == password:
        print('user password')
        session['user'] = user.email
        flash('Logged in!')
        
    else:
        print('no user')
        flash('This email is not recognized in our system')
    
    return redirect('/menu')
  

#cannot click submit button
# @app.route('/time_entry', methods=['POST'])
# def add_sleep_wake_time():
#     """Save sleep and wake time that user submits"""

#     sleep_time = request.form.get('sleep-time')
#     wake_time = request.form.get('wake-time')

#     user_entry = crud.create_user_entry(sleeptime, waketime, sleep_quality, stress_level, energy_level, productivity_level, exercise_level, alcoholic_units)

#     return redirect('/journal_entry')


# @app.route('/journal_entry', methods=['POST'])
# def add_nine_input_fields():
#     """Save 6 slider control inputs and 3 checkbox inputs that user submits"""


#cannot click submit button
@app.route('/log_entry', methods=['POST'])
def add_time_and_input_fields():
    sleeptime = request.form.get('sleeptime')
    waketime = request.form.get('waketime')
    sleep_quality = request.form.get('sleep_quality')
    stress_level = request.form.get('stress')
    energy_level = request.form.get('energy')
    productivity_level = request.form.get('productivity')
    exercise_level = request.form.get('exercise')
    alcoholic_units = request.form.get('alcoholic_units')
    print('received inputs')
    user = crud.get_user_by_email(session['user'])
    user_entry = crud.create_user_entry(user.user_id, sleeptime, waketime, sleep_quality, stress_level, energy_level, productivity_level, exercise_level, alcoholic_units)

    print('user entry', user_entry)
    mood = request.form.get('mood')
    medication = request.form.get('medication')
    symptom = request.form.get('symptom')

    user_entry_mood = crud.create_mood(mood)
    user_entry_medication = crud.create_medication(medication)
    user_entry_symptom = crud.create_symptom(symptom)

    flash("Your entry has been successfully added!")

    return redirect('/menu')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)