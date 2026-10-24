import os
import datetime
import requests
import holidays
import pytz
from requests.auth import HTTPBasicAuth
import dateutil.parser


def handler():
    if is_not_working_day():
        return
    # jm_host = os.environ.get('JM_HOST', '')
    # username = os.environ.get('BASIC_AUTH_USERNAME', '')
    # password = os.environ.get('BASIC_AUTH_PASSWORD', '')
    jm_host = "http://localhost:8080"
    username = "ara"
    password = "ara"
    url = jm_host + '/api/v1/alert'
    params = {'scheduleAt': get_today_alert_date()}
    res = requests.post(url, auth=HTTPBasicAuth(username, password), params=params)
    log = f'{res.status_code} {res.reason}'
    print(log)
    return {
        'status_code': res.status_code,
        'reason': res.reason
    }


def is_not_working_day2():
    kr_holidays = holidays.country_holidays('KR')
    target = dateutil.parser.isoparse('2024-09-15T20:56:35.450686+09:00')
    is_weekend = target.weekday() >= 5  # 5 and 6 correspond to Saturday and Sunday
    is_holiday = target in kr_holidays
    return is_holiday or is_weekend


def is_not_working_day():
    kr_holidays = holidays.country_holidays('KR')
    seoul_tz = pytz.timezone('Asia/Seoul')
    today = datetime.datetime.now(seoul_tz).date()
    is_weekend = today.weekday() >= 5  # 5 and 6 correspond to Saturday and Sunday
    is_holiday = today in kr_holidays
    return is_holiday or is_weekend


def get_today_alert_date():
    seoul_tz = pytz.timezone('Asia/Seoul')
    now = datetime.datetime.now(seoul_tz)
    today_nine_am = datetime.datetime.combine(now.date(), datetime.time(9, 0))
    today_nine_am_seoul = seoul_tz.localize(today_nine_am)
    tomorrow = now.date() + datetime.timedelta(days=1)
    tomorrow_nine_am = datetime.datetime.combine(tomorrow, datetime.time(9, 0))
    tomorrow_nine_am_seoul = seoul_tz.localize(tomorrow_nine_am)
    # iso_format = today_nine_am_seoul.isoformat()
    iso_format = tomorrow_nine_am_seoul.isoformat()
    return iso_format


if __name__ == '__main__':
    print('is_not_working_day ' + is_not_working_day().__str__())
    print('is_not_working_day ' + get_today_alert_date())
    # handler()
