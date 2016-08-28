"""
The flask application package.
"""

from flask import Flask
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://teammaker-bb56c.firebaseio.com', None)

import teammaker.routes