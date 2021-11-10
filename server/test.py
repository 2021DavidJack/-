from flask import Flask,redirect,url_for,request
from flask_cors import *

app=Flask(__name__)
CORS(app,supports_credentials=True)


