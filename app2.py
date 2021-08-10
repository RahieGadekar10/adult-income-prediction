from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

app = Flask(__name__)
model = pickle.load(open('random.pkl', 'rb'))
@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/hi", methods=['POST'])
def pred(): 

    native_country = request.form['native_country']
    workclass = request.form['workclass'] 
    education = request.form['education']
    marital_status = request.form['marital_status']
    occupation = request.form['occupation']
    relationship = request.form['relationship']  
    race = request.form['race']
    age_group = request.form['age_group']    
    educational_num = int(request.form['educational_num'])
    capital_gain = int(request.form['capital_gain'])
    capital_loss = int(request.form['capital_loss'])
    hours_per_week = int(request.form['hours_per_week'])
    age = int(request.form['age'])
    gender = request.form['gender']

    native_country_United_States = 0
    native_country_Others=0    
    if native_country == 'United-States':
        native_country_United_States = 1
        native_country_Others=0
    elif native_country == 'Mexico':
        native_country_United_States = 0
        native_country_Others=0
    else : 
        native_country_United_States = 0
        native_country_Others=1

    if workclass == 'Private' : 
        workclass = 1
    elif workclass == 'Self-emp-not-inc' :
        workclass = 3
    elif workclass == 'Self-emp-inc' :
        workclass = 2
    elif workclass == 'Local-gov'or workclass =='State-gov' or workclass =='Federal-gov' :
        workclass = 5
    elif workclass == 'Without-pay' :
        workclass = 4
    else :
        workclass = 0

    if education== 'Bachelors' :
        education = 1
    elif education == 'HS-grad' :
        education = 4
    elif education == 'Preschool' or education =='11th' or education =='10th' or education =='12th' or education =='1st-4th' or education =='5th-6th' or education =='7th-8th'or education == '9th' :
        education = 6
    elif education == 'Assoc-acdm' or education == 'Assoc-voc' :
        education = 0
    elif education == 'Some-college' :
        education = 2
    elif education == 'Prof-school' :
        education = 5
    else:
        education = 3


    if occupation == 'Tech-support' :
        occupation = 9
    elif occupation == 'Craft-repair' :
        occupation = 2
    elif occupation == 'Other-service' :
        occupation = 6
    elif occupation == 'Sales' :
        occupation = 8
    elif occupation == 'Exec-managerial' :
        occupation = 1
    elif occupation == 'Prof-specialty' :
        occupation = 7
    elif occupation == 'Handlers-cleaners' :
        occupation = 4
    elif occupation == 'Machine-op-inspct' :
        occupation = 5
    elif occupation == 'Adm-clerical' :
        occupation = 0
    elif occupation == 'Farming-fishing' :
        occupation = 3
    elif occupation == 'Transport-moving' :
        occupation = 10
    else:
        occupation = 11


    if relationship== 'Wife' :
        relationship = 5
    elif relationship== 'Own-child' :
        relationship = 3
    elif relationship == 'Husband' :
        relationship = 0
    elif relationship == 'Not-in-family' :
        relationship = 1
    elif relationship == 'Other-relative' :
        relationship = 2
    else :
        relationship = 4   

    if race == 'White': 
        race = 4
    elif race== 'Black' :
        race = 2 
    elif race == 'Asian-Pac-Islander':
        race = 1 
    elif race == 'Amer-Indian-Eskimo' :
        race= 0  
    else : 
        race = 3

    if age_group == 'Adults': 
        age_group_Seniors = 0
        age_group_Adults = 1

    if age_group == 'Seniors': 
        age_group_Seniors = 1
        age_group_Adults = 0
    else : 
        age_group_Seniors = 0
        age_group_Adults = 0
        
    if marital_status == "Widowed" : 
        marital_status_Widowed = 1
        marital_status_Single = 0
        marital_status_Separated = 0

    elif marital_status== "Single" :     
        marital_status_Widowed = 0
        marital_status_Single = 1
        marital_status_Separated = 0
        
    elif marital_status == "Separated" : 
        marital_status_Widowed = 0
        marital_status_Single = 0
        marital_status_Separated = 1
        
    else :         
        marital_status_Widowed = 0
        marital_status_Single = 0
        marital_status_Separated = 0

    if gender == "Male" : 
        gender_Male = 1 
    else : 
        gender_Male = 0
    
    age_hours = hours_per_week * age

    list = [[workclass, education,educational_num,occupation,relationship ,race ,capital_gain,capital_loss,age_hours , marital_status_Separated	,marital_status_Single,	marital_status_Widowed,	gender_Male,native_country_Others,native_country_United_States,age_group_Adults,age_group_Seniors]]
    df = pd.DataFrame(list , columns=['workclass', 'education','educational_num','occupation','relationship' ,'race' ,'capital_gain','capital_loss','age_hours' , 'marital_status_Separated','marital_status_Single','marital_status_Widowed','gender_Male','native_country_Others','native_country_United_States','age_group_Adults','age_group_Seniors'])

    prediction = model.predict(df)
    if prediction == 0 : 
        return render_template("index.html", prediction_text = "Salary Below 50K")
    else : 
        return render_template("index.html", prediction_text = "Salary Above 50K")

if __name__ == "__main__":
    app.run(debug=True)
"""     sc = StandardScaler()
    df = pd.DataFrame(sc.fit_transform(df), columns = df.columns) """


