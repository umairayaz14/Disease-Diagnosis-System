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
usr_budget=10000
usr_city='lahore'
df_hos=pd.read_csv("hos.csv")
df_user=pd.read_csv("users.csv")
df_disease=pd.read_csv("training_data.csv")
cred=["admin","123"]
login_cred=[]
choice=''
choice2=''
choice3=''
#upd_hos=""
#upd_dis="Disease Database"
print(cred[0])
print(cred[1])

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
class Hospitals(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    avg_expense = db.Column(db.Integer)

    def __init__(self,name,city, avg_expense):
        print (name,city,avg_expense)
        self.name = name
        self.city = city
        self.avg_expense = avg_expense

# @app.route('/', methods=['POST','GET'])
# def inex():
#   if request.method=='GET':

#       return render_template("register.html")
#   else:
#       return redirect("syntmos")


@app.route("/symptoms")
def symptoms():
    return render_template("index.html")


@app.route('/result/<data>')
def result(data):
    print ("result data",data)
    data = data.split("&")
    return render_template("result.html", prediction=data[0], hos_list=data[1])
    
@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        response = request.json
        for value in response:
            tmp_dict[value["name"]] = 1
            df = pd.DataFrame([list(tmp_dict.values())])
        current_model_name = 'decision_tree'
        obj = DiseasePrediction(model_name=current_model_name)
        prediction = obj.make_prediction(saved_model_name=current_model_name, test_data=df)
        hos_df=pd.read_csv('hos.csv')
        print("User_city: ", usr_city)
        print("User_budget: ", usr_budget)
        print("Hospitals: ")
        print(hos_df)
        #hos_list=np.array(hos_df.loc[1:])
        for i in range(len(hos_df)):
            if hos_df.loc[i,"avg_expense"]<=usr_budget and hos_df.loc[i,"city"]==usr_city:
                hos_list=np.array(hos_df.loc[i,"name"])
                print('Here: ',hos_list)
        #print(hos_list)
        print("Diseases:",type(prediction))
        print("Diseases:",prediction)
        #print (type(hos_list))
        #print ("hos_list", hos_list.tolist())
        hos_list = list(hos_list.flatten())
        #print ("hos_list",hos_list)
        prediction = list(prediction.flatten())
        response = {"disease":hos_list,"prediction":prediction}
        print (response)
        return jsonify(response)
        #return render_template("result.html", prediction=prediction, hos_list=hos_list)

# user
@app.route('/user', methods = ['GET', 'POST'])
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

#admin
@app.route("/admin", methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        login_uname=request.form["User Name"]
        login_password=request.form["Password"]
        if cred[0]==login_uname and cred[1]==login_password:
            return redirect(url_for('get_update'))
        else:
            return render_template("admin.html")
    else:
        return render_template("admin.html")

#home page
@app.route("/")
def initial():
    return render_template("initial.html")


@app.route("/get_update", methods = ['GET', 'POST'])
def get_update():
    if request.method=="POST":
        choice = str(request.form.get('comp_select'))
        print('In local choice: ',choice)
        url = 'upd/'+choice
        print ("url")
        return redirect(url)
        #return
        #return redirect(url_for('upd',choice=choice))
    else:
        return render_template("update.html")


@app.route("/upd/hospital", methods=['GET','POST'])
def upd1():
     print ("here")
     if request.method=="POST":
        choice2=str(request.form.get('comp_select'))
        print ("in======>", choice2)
        print ("1",request.form['name'])
        print ("2",request.form['city'])
        print ("3",request.form['expense'])
        print ("values: ",request.form['name'],request.form['city'],request.form['expense'])
        hos=Hospitals(request.form['name'],request.form['city'],request.form['expense'])
        # conn=sql.connect('user.sqlite3')
        # cur=conn.cursor()
        h_id=request.form['h_id']
        h_name=request.form['name']
        print('h_name: ',h_name)
        h_city=request.form['city']
        h_exp=request.form['expense']
        print("choice2: ",choice2)
        if choice2=='insert':
            print ("ma enji um",hos)
            db.session.add(hos)
            db.session.commit()
            #cur.execute('insert into Hospital (Name,H_ID,City,Avg_expense) values (h_name,h_id,h_city,h_expense)')
        elif choice2=='delete':
            hos = Hospitals.query.filter_by(id=request.form['h_id']).first()

            print ("start deleting")
            db.session.delete(hos)
            print ("======")
            db.session.commit()
            #cur.execute('delete from Hospital where H_ID = h_id')
        else:
            choice3=str(request.form.get('comp2_select'))
            attr=request.form['attr']
            id2=request.form['h_id2']
            hos_id=Hospitals.query.get(id2)
            print('choice3: ',choice3)
            if choice3=='nm':
                hos_id.name=attr
                db.session.commit()
                #cur.execute('update Hospital set Name=attr where H_ID=id2')
            elif choice3=='city2':
                hos_id.city=attr
                db.session.commit()
                #cur.execute('update Hospital set City=attr where H_ID=id2')
            else:
                hos_id.avg_expense=attr
                db.session.commit()
                #cur.execute('update Hospital set Avg_expense=attr where H_ID=id2')
        return redirect(url_for('get_update'))
     return render_template('hospita_cssl.html')

@app.route("/upd/disease", methods=['GET','POST'])
def upd2():
     if request.method=="POST":
        choice2=str(request.form.get('comp_select'))
        return redirect(url_for('dis_upd',choice2=choice2))
     return render_template('disease.html')
if __name__ == "__main__":
    db.create_all()
    app.run(debug=False)
