"""Script to seed database."""

import os
import json
import random
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()

import crud
import model
import server

os.system('dropdb sleepjournal')
os.system('createdb sleepjournal')

model.connect_to_db(server.app)
model.db.create_all()

#for a user in range 10,
    #WHERE TO PUT THIS? put users in a list and use random choice to associate random data with random users
        #print a fake name, email, password
            #generate 250 entries for each user
                #for each post for each user:
                #generate a sleep time and a wake time
                    #once a sleep time is generated, generate a random number between 5 and 13 hrs
                    #add datetime to random number to get wake time
                #generate 0 - 5 on sleep quality
                #generate 0 - 5 on stress
                #generate 0 - 5 on energy
                #generate 0 - 5 on productivity
                #generate 0 - 5 on exercise
                #generate 0 - 5+ on alcoholic units
                #generate 0-10 on moods
                #generate 0-10 on medications
                #generate 0-9 on symptoms
    

    # how should this data be captured and returned?
    # where to put users in a list and use random choice to associate random data with random users

moods = {
    1: 'Happy', 
    2: 'Calm', 
    3: 'Content', 
    4: 'Excited', 
    5: 'Anxious', 
    6: 'Depressed', 
    7: 'Irritated', 
    8: 'Angry', 
    9: 'Self critical', 
    10: 'Confused', 
}

mood_obj = []

for key in moods:
    mood_dict = random.choice(list(moods.values()))

    mood = model.Mood(mood=mood_dict)
    mood_obj.append(mood)
    model.db.session.add(mood)
    model.db.session.commit()

medications = {
    1: 'None', 
    2: 'Tylenol',
    3: 'Ibuprofen',
    4: 'Decongestant',
    5: 'Cough medicine',
    6: 'Antihistamine',
    7: 'Antacid',
    8: 'Pepto Bismol',
}

medication_obj = []

for key in medications:
    medication_dict = random.choice(list(medications.values()))

    medication = model.Medication(medication=medication_dict)
    medication_obj.append(medication)
    model.db.session.add(medication)
    model.db.session.commit()

symptoms = {
    1: 'None',
    2: 'Fatigue', 
    3: 'Nausea', 
    4: 'Pain', 
    5: 'Headache', 
    6: 'Migrane', 
    7: 'Cold/Flu', 
    8: 'Allergies',
    9: 'Heartburn',
    10: 'Constipation', 
    11: 'Diarrhea', 
    12: 'Bloating', 
}

symptom_obj = []

for key in symptoms:
    symptom_dict = random.choice(list(symptoms.values()))

    symptom = model.Symptom(symptom=symptom_dict)
    symptom_obj.append(symptom)
    model.db.session.add(symptom)
    model.db.session.commit()


for user in range(10):
    name = fake.name()
    email = fake.email(domain=None)
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

    user = model.User(full_name=name, email=email, password=password)
    model.db.session.add(user)
    model.db.session.commit()

    for user_entry in range(250):
        # start = datetime.fromisoformat('2019-01-01')
        start = datetime(2019, 1, 1, 0, 0, 0, 0)
        # end = datetime.fromisoformat('2019-12-31')
        end = datetime(2019, 12, 31, 23, 59, 59, 0)

        sleeptime = fake.date_time_between_dates(datetime_start=start, datetime_end=end)

        random_sleep_hrs = random.randint(4, 12)

        waketime = sleeptime + timedelta(hours=random_sleep_hrs)
        
        # waketime = sleeptime + timedelta(hours=9)
    
        sleep_quality = random.randint(0, 5)
    
        stress_level = random.randint(0, 5)

        energy_level = random.randint(0, 5)
    
        productivity_level = random.randint(0, 5)

        exercise_level = random.randint(0, 5)
    
        list_of_alcoholic_units = ['0', '1', '2', '3', '4', '5+']
        random.choice(list_of_alcoholic_units)

        user_entry = model.User_entry(user_id=user.user_id, sleeptime=sleeptime, waketime=waketime, sleep_quality=sleep_quality, stress_level=stress_level, energy_level=energy_level, productivity_level=productivity_level, exercise_level=exercise_level, alcoholic_units=list_of_alcoholic_units)
        model.db.session.add(user_entry)
        model.db.session.commit()

        random_num_moods_added = random.randint(0, 5)
        for _ in range(random_num_moods_added):
            random_mood = random.choice(mood_obj)
        
            user_entry_mood = model.User_entry_mood(user_entry_id=user_entry.user_entry_id, mood_id=random_mood.mood_id)
            model.db.session.add(user_entry_mood)
            model.db.session.commit()
        
        random_num_medications_added = random.randint(0, 1)
        for _ in range(random_num_medications_added):
            random_medication = random.choice(medication_obj)
        
            user_entry_medication = model.User_entry_medication(user_entry_id=user_entry.user_entry_id, medication_id=random_medication.medication_id)
            model.db.session.add(user_entry_medication)
            model.db.session.commit()

        random_num_symptoms_added = random.randint(0, 2)
        for _ in range(random_num_symptoms_added):
            random_symptom = random.choice(symptom_obj)
            
            user_entry_symptom = model.User_entry_symptom(user_entry_id=user_entry.user_entry_id, symptom_id=random_symptom.symptom_id)
            model.db.session.add(user_entry_symptom)
            model.db.session.commit()


        # sleeptime = db.Column(db.DateTime)
        # waketime = db.Column(db.DateTime)
        # sleep_quality = db.Column(db.Integer, nullable=False)
        # stress_level = db.Column(db.Integer)
        # energy_level = db.Column(db.Integer)
        # productivity_level = db.Column(db.Integer)
        # exercise_level = db.Column(db.Integer)
        # alcoholic_units = db.Column(db.Integer)


