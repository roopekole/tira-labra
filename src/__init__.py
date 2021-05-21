# Import flask and flask-session
from flask import Flask, session
app = Flask(__name__)

from src import views
