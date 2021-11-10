from flask import Flask,redirect,url_for,request
from flask_cors import *
from database import database
app=Flask(__name__)
CORS(app,supports_credentials=True)


@app.route('/api/user/extend/updatePersonalHealthData',methods=['POST'])
def updatePersonalHealthData():
	if request.headers['Content-Type']=="multipart/form-data":
		UserExtend=request.form['UserExtend']
		User=request.form['User']
		HealthData=request.form['HealthData']
		result=database.updatePersonalHealthData(UserExtend,User,HealthData)
		if result:
			print("login success!")
			return {'errcode':0,
				'errmsg':'修改成功'
			},200
		else:
			print("login failed!")
			return {'errcode':400,
				'errmsg':'用户不存在或未知错误'
			},400
	else:
		return {'errcode':400,
				'errmsg':'请求类型错误'
			},400

@app.route('/api/user/extend/updateSleepData',methods=['POST'])
def updateSleepData():
	if request.headers['Content-Type']=="multipart/form-data":
		UserExtend=request.form['UserExtend']
		User=request.form['User']
		SleepData=request.form['SleepData']
		result=database.updateSleepData(UserExtend,User,SleepData)
		if result:
			print("login success!")
			return {'errcode':0,
				'errmsg':'修改成功'
			},200
		else:
			print("login failed!")
			return {'errcode':400,
				'errmsg':'用户不存在或未知错误'
			},400
	else:
		return {'errcode':400,
				'errmsg':'请求类型错误'
			},400
