from config import db
import pymysql
import json
conn = pymysql.connect(host=db['host'], user=db['user'], passwd=db['passwd'],
                       database=db['database'],
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
db = conn.cursor()


def updateSleepData(UserExtend, User, SleepData):
    uid = User['uid']
    sleepdata1 = SleepData['healthdata1']
    userextend1 = UserExtend['userextend1']
    db.execute('UPDATE SleepData SET sleepdata1=%s WHERE uid=%s', (sleepdata1, uid))
    return db.rowcount


def updatePersonalHealthData(UserExtend, User, HealthData):
    uid = User['uid']
    healthdata1 = HealthData['healthdata1']
    userextend1 = UserExtend['userextend1']
    db.execute('UPDATE HealthData SET healthdata1=%s WHERE uid=%s', (healthdata1, uid))
    return db.rowcount


def deletePersonalHealthData(UserExtend, User, HealthData):
    uid = User['uid']
    healthdata1 = HealthData['healthdata1']
    userextend1 = UserExtend['userextend1']
    db.execute('DELETE FROM HealthData  WHERE uid=%s', (uid,))
    return db.rowcount


def deleteSleepData(UserExtend, User, SleepData):
    uid = User['uid']
    sleepdata1 = SleepData['healthdata1']
    userextend1 = UserExtend['userextend1']
    db.execute('DELETE FROM SleepData  WHERE uid=%s', (uid,))
    return db.rowcount


def timeSensitiveReminder(UserExtend, User, Reminder):
    uid = User['uid']
    remainder1 = Reminder['remainder1']
    userextend1 = UserExtend['userextend1']
    db.execute('INSERT INTO Reminder (healthdata1,) VALUES(%s,%s)', (remainder1, uid))
    return db.rowcount


def clearTimeSensitiveReminder(UserExtend, User, Reminder):
    uid = User['uid']
    ramaind1 = Reminder['ramaind1']
    userextend1 = UserExtend['userextend1']
    db.execute('DELETE FROM Reminder  WHERE uid=%s', (uid,))
    return db.rowcount


def collectSleepData(UserExtend, User, SleepData):

    return True


def getSleepData(UserExtend, User, SleepData):
    return True


def addPersonalHealthData(UserExtend, User, HealthData):
    return True


def getPersonalHealthData(UserExtend, User, HealthDataCondition):
    return True


def getSleepMusic(UserExtend, User, SleepMusic):
    return True


def storageMessagePopup(UserExtend, User, MessagePopup):
    return True


def addMarketingPromotion(UserExtend, User, Promotion):
    return True