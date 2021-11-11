from flask import request
from ..database import database
from . import extend


@extend.route('/api/user/extend/<string:uri>', methods=['POST'])
def extendOperate(uri):
    if request.headers['Content-Type'] == "multipart/form-data":
        UserExtend = request.form['UserExtend']
        User = request.form['User']
        if uri in ['updatePersonalHealthData',
                   'deletePersonalHealthData',
                   'addPersonalHealthData']:
            HealthData = request.form['HealthData']
            if uri == 'updatePersonalHealthData':
                result = database.updatePersonalHealthData(UserExtend, User, HealthData)
            elif uri == 'deletePersonalHealthData':
                result = database.deletePersonalHealthData(UserExtend, User, HealthData)
            elif uri == 'addPersonalHealthData':
                result = database.addPersonalHealthData(UserExtend, User, HealthData)
            else:
                result = None
        elif uri in ['updateSleepData',
                     'deleteSleepData',
                     'collectSleepData',
                     'getSleepData']:
            SleepData = request.form['SleepData']
            if uri == 'updateSleepData':
                result = database.updateSleepData(UserExtend, User, SleepData)
            elif uri == 'deleteSleepData':
                result = database.deleteSleepData(UserExtend, User, SleepData)
            elif uri == 'collectSleepData':
                result = database.collectSleepData(UserExtend, User, SleepData)
            elif uri == 'getSleepData':
                result = database.getSleepData(UserExtend, User, SleepData)
            else:
                result = None
        elif uri == 'getPersonalHealthData':
            HealthDataCondition = request.form['HealthDataCondition']
            result = database.getPersonalHealthData(UserExtend, User, HealthDataCondition)
        elif uri in ['timeSensitiveReminder', 'clearTimeSensitiveReminder']:
            Reminder = request.form['Reminder']
            if uri == 'timeSensitiveReminder':
                result = database.timeSensitiveReminder(UserExtend, User, Reminder)
            else:
                result = database.clearTimeSensitiveReminder(UserExtend, User, Reminder)
        elif uri == 'SleepMusic':
            SleepMusic = request.form['SleepMusic']
            result = database.getSleepMusic(UserExtend, User, SleepMusic)
        elif uri == 'MessagePopup':
            MessagePopup = request.form['MessagePopup']
            result = database.storageMessagePopup(UserExtend, User, MessagePopup)
        elif uri == 'addMarketingPromotion':
            Promotion = request.form['Promotion']
            result = database.addMarketingPromotion(UserExtend, User, Promotion)
        else:
            result = None
        if result:
            return {'errcode': 0, 'errmsg': '修改成功'}, 200
        else:
            return {'errcode': 400, 'errmsg': '用户不存在或未知错误'}, 400
    else:
        return {'errcode': 400, 'errmsg': '请求类型错误'}, 400
