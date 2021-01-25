import os
import time
import schedule


# to be modified
def dump_job(host, user, password, db_name):
    time_string = time.strftime('%Y%m%d%H%M%S')
    print(time_string)
    print('start..')
    folder_name = db_name
    file_name = db_name + '.' + time_string + '.sql'
    cmd = f'mysqldump -h {host} -u {user} --password={password} {db_name} > {folder_name}\\{file_name}'
    os.system(cmd)


schedule.every().day.at('13:05').do(dump_job, host='10.210.201.12', user='admin', password='20180105', db_name='mssqlj3ydb')

while True:
    schedule.run_pending()
    time.sleep(1)
