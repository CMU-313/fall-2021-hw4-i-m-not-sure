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

To query the microservice, include the above parameters in the url with correct data type and range. For example, http://localhost:5000/predict?age=18&&absences=6&&health=3&&Medu=4&&Fedu=4&&studytime=2&&traveltime=2. 

## Model Output 

The model output a binary value (0 or 1) which predicts wheter or not the student is going to be a quality student. Quality students are those who score 15 or higher (out of 20) on the final grade.

## Model Justification 

The retrained model uses the features above to train and predict quality students. The new model is able to achieve 98.63% accuracy in predicting the train data's output. This model outperforms the baseline model (with 51.85% accuracy) by incorporating 4 additional features to train the model. (add more justification)

## Deploying the Microservice 

(add deployment instructions)

## Testing 

(add explanation and justification of the tests done)
