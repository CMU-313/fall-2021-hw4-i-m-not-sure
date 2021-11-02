from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     age = request.args.get('age')
     absences = request.args.get('absences')
     health = request.args.get('health')
     Medu = request.args.get('Medu')
     Fedu = request.args.get('Fedu')
     studytime = request.args.get('studytime')
     traveltime = request.args.get('traveltime')
     #data = [[age],[health],[absences]]
     query_df = pd.DataFrame({ 'health' : pd.Series(health) ,
                         'Medu' : pd.Series(Medu) ,
                         'Fedu' : pd.Series(Fedu),
                         'studytime' : pd.Series(studytime) ,
                         'traveltime' : pd.Series(traveltime) ,
                         'absences' : pd.Series(absences), 
                         'age' : pd.Series(age)})
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)