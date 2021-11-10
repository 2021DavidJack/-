from flask import Flask,redirect,url_for,request
from flask_cors import *

app=Flask(__name__)
CORS(app,supports_credentials=True)


@app.route('/api/user/extend/updatePersonalHealthData',methods=['POST'])
def updatePersonalHealthData():
	if request.headers['Content-Type']=="multipart/form-data":
		UserExtend=request.form['UserExtend']
		User=request.form['User']
		HealthData=request.form['HealthData']