# Software Engineering for Machine Learning Assignment

## Model Input

To use the model, the query must contain the at least the following parameters:

1. Age: student's age (numeric)
2. Absences: number of school absences (numeric)
3. Health: student's health status (numeric from 1 - very bad 5 - very good)
4. Medu: mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education)
5. Fedu: father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education)
6. Studytime: weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
7. Traveltime: home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)

To query the microservice, include the above parameters in the url with correct data type and range. 
For example, http://localhost:5000/predict?age=18&&absences=6&&health=3&&Medu=4&&Fedu=4&&studytime=2&&traveltime=2. 


## Model Output 

The model output a binary value (0 or 1) which predicts wheter or not the student is going to be a quality student. Quality students are those who score 15 or higher (out of 20) on the final grade.

## Model Justification 

The retrained model uses the features above to train and predict quality students. The new model is able to achieve 98.63% accuracy in predicting the train data's output. This model outperforms the baseline model (with 51.85% accuracy) by incorporating 4 additional features to train the model. 

Additional features are Medu, Fedu, Studytime, Traveltime which are important features to build high-quality students(add more justification)

## Deploying the Microservice 

Microservice is based on a flask app. To build the app the following steps should be followed:
1. Clone repository
2. Within `dockerfile` directory, run the following docker command `docker build -t ml:latest .`
3. Upon successful build, call `docker run -d -p 5000:5000 ml` to create an instance of the flask application.
4. If the instance is up and running, calling `curl http://localhost:5000` should return `try the predict route it is great!`
5. The endpoint for the microservice is available at `http://localhost:5000/predict?`
6. Args that must be passed to the endpoint are `age,absences,health,Medu,Fedu,studytime,traveltime`
## Testing 

The test file using pytest can be found in dockerfile/test_app.py. To run the test, in dockerfile directory use python3 -m pytest -v.

The tests include the following: 
1. Sanity check that the site is up after deployment. This test checks that after starting the session we get a 200 response. 
2. Empty arguments. Model cannot predict without any input. This test should check that an error is raised when empty argument is passed. 
3. Not enough arguments. Since the model predicts the result based on 7 features, these must be provided to the model. If not enough arguments are given, the query should fail. 
4. Test result is 0. When given the features that model should predict to have 0 output, the response should reflect that. 
5. Test result is 1. When given the features that model should predict to have 1 output, the response should reflect that.
6. Extra arguments. If the minimum 7 features are given, the model should be able to predict regardless of any extra arguments given and not raise an error. 
7. Consistency test. To check that the application returns consistent result, given multiple queries with the same arguments, the result should be the same. 


