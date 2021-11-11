from config import db
import pymysql

conn = pymysql.connect(host=db['host'], user=db['user'], passwd=db['passwd'],
                       database=db['database'],
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
db = conn.cursor()


def updateSleepData(UserExtend, User, SleepData):
    return True


def updatePersonalHealthData(UserExtend, User, HealthData):
    return True


def deletePersonalHealthData(UserExtend, User, HealthData):
    return True


def deleteSleepData(UserExtend, User, SleepData):
    return True


def timeSensitiveReminder(UserExtend, User, Reminder):
    return True


def collectSleepData(UserExtend, User, SleepData):
    return True


def getSleepData(UserExtend, User, SleepData):
    return True


def addPersonalHealthData(UserExtend, User, HealthData):
    return True


def getPersonalHealthData(UserExtend, User, HealthDataCondition):
    return True


def clearTimeSensitiveReminder(UserExtend, User, Reminder):
    return True


def getSleepMusic(UserExtend, User, SleepMusic):
    return True


def storageMessagePopup(UserExtend, User, MessagePopup):
    return True


def addMarketingPromotion(UserExtend, User, Promotion):
    return True