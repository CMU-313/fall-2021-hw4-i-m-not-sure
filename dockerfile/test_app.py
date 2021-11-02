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


PREDICT_URL = 'http://localhost:5000/'

def init_db(app):
    print(app)
    if "db" not in g:
        g.db = sqlite3.connect(
            app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

@pytest.fixture
def client():
    http_session = requests.Session()
    retries = Retry(total=10, backoff_factor=0.1)
    http_session.mount('http://', HTTPAdapter(max_retries=retries))
    return http_session

def test_empty_request(client):
    response = client.get(PREDICT_URL)
    print("here" + response.text)
    assert response.status_code == 200


if __name__ == "__main__":
    http_session = requests.Session()
    retries = Retry(total=10, backoff_factor=0.1)
    http_session.mount('http://', HTTPAdapter(max_retries=retries))
    response = http_session.get(PREDICT_URL)
    print(response.text)
