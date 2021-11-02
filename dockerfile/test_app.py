import os
import tempfile
import sqlite3
import requests
import json
import pytest

from flask import Flask
from flask import g
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def init_db(app):
    print(app)
    if "db" not in g:
        g.db = sqlite3.connect(
            app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

BASE_URL = 'http://localhost:5000/'
PREDICT_URL = 'http://localhost:5000/predict?'
@pytest.fixture
def client():
    http_session = requests.Session()
    retries = Retry(total=10, backoff_factor=0.1)
    http_session.mount('http://', HTTPAdapter(max_retries=retries))
    return http_session

def test_flask_is_up(client):
    response = client.get(BASE_URL)
    assert response.status_code == 200
    assert response.text == "try the predict route it is great!"

def test_predict_empty_request(client):
    response = client.get(PREDICT_URL)
    assert response.status_code == 500

def test_predict_insufficent_args(client):
    response = client.get(PREDICT_URL + "age=18&&health=3&&Medu=1")
    assert response.status_code == 500

def test_predict_model_too_many_args(client):
    response = client.get(PREDICT_URL + "age=18&&absences=6&&health=3&&Medu=4&&Fedu=4&&studytime=2&&traveltime=2&&random1=a&&random2=b&&random3=4")
    assert response.status_code == 200
    assert response.text == '0\n'

def test_predict_model_correct_output(client):
    response = client.get(PREDICT_URL + "age=18&&absences=6&&health=3&&Medu=4&&Fedu=4&&studytime=2&&traveltime=2")
    assert response.status_code == 200
    assert response.text == '0\n'

def test_flask_and_model_consistency(client):
    for i in range(10):
        response = client.get(PREDICT_URL + "age=18&&absences=6&&health=3&&Medu=4&&Fedu=4&&studytime=2&&traveltime=2")
        assert response.status_code == 200
        assert response.text == '0\n'

if __name__ == "__main__":
    http_session = requests.Session()
    retries = Retry(total=10, backoff_factor=0.1)
    http_session.mount('http://', HTTPAdapter(max_retries=retries))
    response = http_session.get(PREDICT_URL)
    print(response.status_code)
    print(response.text)