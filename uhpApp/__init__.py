from flask import Flask
from uhpApp.config import config

#Register the app
app = Flask(__name__)
app.secret_key = config['sec_key']

from uhpApp import routes
