from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app


@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            # Reading form data from the POST request
            Marital_status =float(request.form['Marital_status'])
            House_Ownership =float(request.form['House_Ownership'])
            Car_Ownership =float(request.form['Car_Ownership'])
            Profession =float(request.form['Profession'])
            CITY =float(request.form['CITY'])
            STATE =float(request.form['STATE'])
            CURRENT_HOUSE_YRS =float(request.form['CURRENT_HOUSE_YRS'])
            Age_band=float(request.form['Age_band'])
            Total_EXP =float(request.form['Total_EXP'])
            
            
            data = [Marital_status,House_Ownership,Car_Ownership,Profession,CITY,STATE,CURRENT_HOUSE_YRS,Age_band,Total_EXP]
            data = np.array(data).reshape(1, 9)
            # Making predictions using the PredictionPipeline
            obj = PredictionPipeline()
            predict = obj.predict(data)
            # Rendering the template with the prediction result
            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
        # This block is executed when the route is accessed with a GET request.
        # Rendering the 'index.html' template for GET requests.
    else:
        return render_template('index.html')

if __name__ == "__main__":
	    app.run(host="0.0.0.0", port = 8080)