from config import db
import pymysql

conn = pymysql.connect(host=db['host'], user=db['user'], passwd=db['passwd'], database=db['database'], charset='utf8',cursorclass = pymysql.cursors.DictCursor)
cursor = conn.cursor()
db=conn.cursor()

def upupdatePersonalHealthData(UserExtend,User,HealthData):
	return True;

def updateSleepData(UserExtend,User,SleepData):
	return True;