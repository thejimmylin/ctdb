import os
import time
import schedule
import json


with open(r'..\..\secrets.json') as f:
    s = f.read()

d = json.loads(s)
PYTHONPATH_ABS = d['PYTHONPATH_ABS']
REPO_ROOT = d['REPO_ROOT']


def calld_django_send_diary_user_email():
    time_string = time.strftime('%Y%m%d%H%M%S')
    print(time_string)  # This would not show on windows 10 cmd, to be fixed.
    print('start..')  # This would not show on windows 10 cmd, to be fixed.
    cmd = f'{PYTHONPATH_ABS} {REPO_ROOT}\\manage.py senddiaryuseremail'
    os.system(cmd)


schedule.every().day.at('11:17').do(calld_django_send_diary_user_email)

while True:
    schedule.run_pending()
    time.sleep(1)
