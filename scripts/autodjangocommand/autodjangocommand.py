import os
import time
import schedule


def calld_django_send_diary_user_email():
    time_string = time.strftime('%Y%m%d%H%M%S')
    print(time_string)
    print('start..')
    cmd = r'call C:\Users\jimmy_lin\repos\ctdb\.venv\Scripts\activate'
    os.system(cmd)
    cmd = r'python C:\Users\jimmy_lin\repos\ctdb\manage.py senddiaryuseremail'
    os.system(cmd)


schedule.every().day.at('16:20').do(calld_django_send_diary_user_email)

while True:
    schedule.run_pending()
    time.sleep(1)
