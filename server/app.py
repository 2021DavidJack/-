from flask import Flask, redirect, url_for, request
from api.user import extend
from flask_cors import *
from api.database import database
app = Flask(__name__)
CORS(app, supports_credentials=True)



