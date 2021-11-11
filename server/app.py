from flask import Flask, redirect, url_for, request
from flask_cors import *
from api.database import database
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/api/user/extend/updatePersonalHealthData', methods=['POST'])
def updatePersonalHealthData():
	if request.headers['Content-Type'] == "multipart/form-data":
		UserExtend = request.form['UserExtend']
		User = request.form['User']
		HealthData = request.form['HealthData']
		result = database.updatePersonalHealthData(UserExtend, User, HealthData)
		if result:
			return {'errcode': 0, 'errmsg': '修改成功'}, 200
		else:
			return {'errcode': 400, 'errmsg': '用户不存在或未知错误'}, 400
	else:
		return {'errcode': 400, 'errmsg': '请求类型错误'}, 400

@app.route('/api/user/extend/updateSleepData', methods=['POST'])
def updateSleepData():
	if request.headers['Content-Type'] == "multipart/form-data":
		UserExtend = request.form['UserExtend']
		User = request.form['User']
		SleepData = request.form['SleepData']
		result = database.updateSleepData(UserExtend, User, SleepData)
		if result:
			return {'errcode': 0, 'errmsg': '修改成功'}, 200
		else:
			return {'errcode': 400, 'errmsg': '用户不存在或未知错误'}, 400
	else:
		return {'errcode': 400, 'errmsg': '请求类型错误'}, 400

@app.route('/api/user/extend/deletePersonalHealthData', methods=['POST'])
def deletePersonalHealthData():
	if request.headers['Content-Type'] == "multipart/form-data":
		UserExtend = request.form['UserExtend']
		User = request.form['User']
		HealthData = request.form['HealthData']
		result = database.deletePersonalHealthData(UserExtend, User, HealthData)
		if result:
			return {'errcode': 0, 'errmsg': '删除成功'}, 200
		else:
			return {'errcode': 400, 'errmsg': '用户不存在或未知错误'}, 400
	else:
		return {'errcode': 400, 'errmsg': '请求类型错误'}, 400

@app.route('/api/user/extend/deleteSleepData', methods=['POST'])
def deleteSleepData():
	if request.headers['Content-Type'] == "multipart/form-data":
		UserExtend = request.form['UserExtend']
		User = request.form['User']
		SleepData = request.form['SleepData']
		result = database.deleteSleepData(UserExtend, User, SleepData)
		if result:
			return {'errcode': 0, 'errmsg': '删除成功'}, 200
		else:
			return {'errcode': 400, 'errmsg': '用户不存在或未知错误'}, 400
	else:
		return {'errcode': 400, 'errmsg': '请求类型错误'}, 400

@app.route('/api/user/extend/timeSensitiveReminder', methods=['POST'])
def timeSensitiveReminder():
	if request.headers['Content-Type'] == "multipart/form-data":
		UserExtend = request.form['UserExtend']
		User = request.form['User']
		Reminder = request.form['Reminder']
		result = database.timeSensitiveReminder(UserExtend, User, Reminder)
		if result:
			return {'errcode': 0, 'errmsg': '删除成功'}, 200
		else:
			return {'errcode': 400, 'errmsg': '用户不存在或未知错误'}, 400
	else:
		return {'errcode': 400, 'errmsg': '请求类型错误'}, 400

@app.route('/api/user/extend/collectSleepData',methods=['POST'])
def collectSleepData():
	if request.headers['Content-Type'] == "multipart/form-data":
		UserExtend = request.form['UserExtend']
		User = request.form['User']
		SleepData = request.form['SleepData']
		result = database.collectSleepData(UserExtend, User, SleepData)
		if result:
			return {'errcode': 0, 'errmsg': '录入成功'}, 200
		else:
			return {'errcode': 400, 'errmsg': '用户不存在或未知错误'}, 400
	else:
		return {'errcode': 400, 'errmsg': '请求类型错误'}, 400

@app.route('/api/user/extend/getSleepData',methods=['POST'])
def getSleepData():
	if request.headers['Content-Type'] == "multipart/form-data":
		UserExtend = request.form['UserExtend']
		User = request.form['User']
		SleepData = request.form['SleepData']
		result = database.getSleepData(UserExtend, User, SleepData)
		if result:
			return {'SleepData': result, 'errmsg': '录入成功'}, 200
		else:
			return {'errcode': 400, 'errmsg': '用户不存在或未知错误'}, 400
	else:
		return {'errcode': 400, 'errmsg': '请求类型错误'}, 400
