# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:12:38 2021

@author: Ghulam Gharibi
"""

from flask import Flask, render_template, request,jsonify, redirect, flash, url_for
import pandas as pd
import numpy as np
import sqlite3 as sql
df_hos=pd.read_csv("Hospital.csv")
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
app=Flask(__name__)
@app.route("/", methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        login_uname=request.form["User Name"]
        login_password=request.form["Password"]
        if cred[0]==login_uname and cred[1]==login_password:
            return redirect(url_for('success'))
        else:
            return render_template("admin.html")
    else:
        return render_template("admin.html")
@app.route("/success")
def success():
    return render_template("update.html")

@app.route("/get_update", methods = ['GET', 'POST'])
def get_update():
    if request.method=="POST":
        choice = str(request.form.get('comp_select'))
        print('In local choice: ',choice)
        url = 'upd/'+choice
        print ("url")
        return redirect(url)

        #return redirect(url_for('upd',choice=choice))
    else:
        return render_template("update.html")


@app.route("/upd/hospital", methods=['GET','POST'])
def upd1():
     if request.method=="POST":
        choice2=str(request.form.get('comp_select'))
        print ("======>", choice2)
        return redirect(url_for('hos_upd',choice2=choice2))
     return render_template('hospital.html')
 
@app.route("/upd/disease", methods=['GET','POST'])
def upd2():
     if request.method=="POST":
        choice2=str(request.form.get('comp_select'))
        return redirect(url_for('dis_upd',choice2=choice2))
     return render_template('disease.html')
"""    
@app.route("/upd", methods=['GET','POST'])
def upd():
    choice_tmp = request.args['choice']
    if request.method=="POST":
        choice2=str(request.form.get('comp_select'))
        #ch=request.args.get('cho')
        print('Choice: ',choice_tmp)
        print('choice2: ',choice2)
        if choice_tmp=='hospital':
            return redirect(url_for('hos_upd',choice2=choice2))
        else:
            return redirect(url_for('dis_upd'))
    else:
        return render_template('upd.html')
"""  
    
@app.route("/hos_upd", methods=['GET','POST'])
def hos_upd():
    if request.method=="POST":
        conn=sql.connect('user.sqlite3')
        cur=conn.cursor()
        h_id=request.form['h_id']
        h_name=request.form['name']
        h_city=request.form['city']
        h_exp=request.form['expense']
        print("choice2: ",choice2)
        if choice2=='insert':
            cur.execute('insert into Hospital (Name,H_ID,City,Avg_expense) values (h_name,h_id,h_city,h_expense)')
        elif choice2=='delete':
            cur.execute('delete from Hospital where H_ID = h_id')
        else:
            choice3=str(request.form.get('comp_select'))
            attr=request.form['attr']
            id2=request.form['h_id2']
            if choice3=='nm':
                cur.execute('update Hospital set Name=attr where H_ID=id2')
            elif choice3=='city2':
                cur.execute('update Hospital set City=attr where H_ID=id2')
            else:
                cur.execute('update Hospital set Avg_expense=attr where H_ID=id2')
                return redirect(url_for('success'))
    else:
        print ("after hospital")
        return render_template("hos_upd.html")
@app.route('/dis_upd',methods = ['GET', 'POST'])
def dis_upd():
    if request.method=='POST':
        print ("pass")
    else:
        return render_template('dis_upd.html')
        
if __name__ == "__main__":
   # db.create_all()
    app.run(debug=False)