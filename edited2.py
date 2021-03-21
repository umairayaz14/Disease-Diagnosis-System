from flask import Flask, render_template, request,jsonify, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from main import DiseasePrediction
import sqlite3
import numpy as np
#import hospital_list

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'
app.config['SECRET_KEY'] = "SECRET_KEY"
tmp_dict = {'itching':0, 'skin_rash': 0, 'nodal_skin_eruptions': 0, 'continuous_sneezing': 0, 'shivering': 0, 'chills': 0, 'joint_pain': 0, 'stomach_pain': 0, 'acidity': 0, 'ulcers_on_tongue': 0, 'muscle_wasting': 0, 'vomiting': 0, 'burning_micturition': 0, 'spotting_ urination': 0, 'fatigue': 0, 'weight_gain': 0, 'anxiety': 0, 'cold_hands_and_feets': 0, 'mood_swings': 0, 'weight_loss': 0, 'restlessness': 0, 'lethargy': 0, 'patches_in_throat': 0, 'irregular_sugar_level': 0, 'cough': 0, 'high_fever': 0, 'sunken_eyes': 0, 'breathlessness': 0, 'sweating': 0, 'dehydration': 0, 'indigestion': 0, 'headache': 0, 'yellowish_skin': 0, 'dark_urine': 0, 'nausea': 0, 'loss_of_appetite': 0, 'pain_behind_the_eyes': 0, 'back_pain': 0, 'constipation': 0, 'abdominal_pain': 0, 'diarrhoea': 0, 'mild_fever': 0, 'yellow_urine': 0, 'yellowing_of_eyes': 0, 'acute_liver_failure': 0, 'fluid_overload': 0, 'swelling_of_stomach': 0, 'swelled_lymph_nodes': 0, 'malaise': 0, 'blurred_and_distorted_vision': 0, 'phlegm': 0, 'throat_irritation': 0, 'redness_of_eyes': 0, 'sinus_pressure': 0, 'runny_nose': 0, 'congestion': 0, 'chest_pain': 0, 'weakness_in_limbs': 0, 'fast_heart_rate': 0, 'pain_during_bowel_movements': 0, 'pain_in_anal_region': 0, 'bloody_stool': 0, 'irritation_in_anus': 0, 'neck_pain': 0, 'dizziness': 0, 'cramps': 0, 'bruising': 0, 'obesity': 0, 'swollen_legs': 0, 'swollen_blood_vessels': 0, 'puffy_face_and_eyes': 0, 'enlarged_thyroid': 0, 'brittle_nails': 0, 'swollen_extremeties': 0, 'excessive_hunger': 0, 'extra_marital_contacts': 0, 'drying_and_tingling_lips': 0, 'slurred_speech': 0, 'knee_pain': 0, 'hip_joint_pain': 0, 'muscle_weakness': 0, 'stiff_neck': 0, 'swelling_joints': 0, 'movement_stiffness': 0, 'spinning_movements': 0, 'loss_of_balance': 0, 'unsteadiness': 0, 'weakness_of_one_body_side': 0, 'loss_of_smell': 0, 'bladder_discomfort': 0, 'foul_smell_of urine': 0, 'continuous_feel_of_urine': 0, 'passage_of_gases': 0, 'internal_itching': 0, 'toxic_look_(typhos)': 0, 'depression': 0, 'irritability': 0, 'muscle_pain': 0, 'altered_sensorium': 0, 'red_spots_over_body': 0, 'belly_pain': 0, 'abnormal_menstruation': 0, 'dischromic _patches': 0, 'watering_from_eyes': 0, 'increased_appetite': 0, 'polyuria': 0, 'family_history': 0, 'mucoid_sputum': 0, 'rusty_sputum': 0, 'lack_of_concentration': 0, 'visual_disturbances': 0, 'receiving_blood_transfusion': 0, 'receiving_unsterile_injections': 0, 'coma': 0, 'stomach_bleeding': 0, 'distention_of_abdomen': 0, 'history_of_alcohol_consumption': 0, 'fluid_overload.1': 0, 'blood_in_sputum': 0, 'prominent_veins_on_calf': 0, 'palpitations': 0, 'painful_walking': 0, 'pus_filled_pimples': 0, 'blackheads': 0, 'scurring': 0, 'skin_peeling': 0, 'silver_like_dusting': 0, 'small_dents_in_nails': 0, 'inflammatory_nails': 0, 'blister': 0, 'red_sore_around_nose': 0, 'yellow_crust_ooze': 0}

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    city = db.Column(db.String(50))
    budget = db.Column(db.String(200)) 
    age = db.Column(db.String(10))

    def __init__(self, fname,lname, city, budget,age):
        self.fname = fname
        self.lname = lname
        self.city = city
        self.budget = budget
        self.age = age

# @app.route('/', methods=['POST','GET'])
# def inex():
#   if request.method=='GET':

#       return render_template("register.html")
#   else:
#       return redirect("syntmos")

usr_budget=50000
usr_city="Quetta"
@app.route("/symptoms")
def symptoms():
    return render_template("index.html")
    
@app.route('/test', methods=['POST','GET'])
def test():
    # print("Kareema")
    response = request.json
    for value in response:
        # print (value["name"])
        # print (tmp_dict[value["name"]])
        tmp_dict[value["name"]] = 1
    df = pd.DataFrame([list(tmp_dict.values())])
    current_model_name = 'decision_tree'
    obj = DiseasePrediction(model_name=current_model_name)
    prediction = obj.make_prediction(saved_model_name=current_model_name, test_data=df)
    hos_df=pd.read_csv('Hospital.csv')
    print("User_city: ", usr_city)
    print("User_budget: ", usr_budget)
    print("Hospitals: ")
    print(hos_df)
    for i in range(len(hos_df)):
        if hos_df.loc[i,"Avg_expense"]<=usr_budget and hos_df.loc[i,"City"]==usr_city:
            #print(hos_df.loc[i,"Name"])
            hos_list=np.array(hos_df.loc[i,"Name"])
            print(hos_list)
            print("Diseases:")
            print(prediction)
    #return prediction[0]
    return render_template("result.html", prediction=prediction, hos_list=hos_list)
@app.route('/', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['fname'] or not request.form['lname'] or not request.form['city'] or not request.form['budget'] or not request.form['age']:
            flash('Please enter all the fields', 'error')
        else:
            user = Users(request.form['fname'], request.form['lname'],request.form['city'],
            request.form['budget'], request.form['age'])
            usr_budget=request.form['budget']
            usr_city=request.form['lname']
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('symptoms'))
    return render_template('register.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=False)
