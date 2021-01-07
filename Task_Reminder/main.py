from numpy.lib.shape_base import tile
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import time
from datetime import datetime
from plyer import notification
import pyttsx3


def clean_time(t,m):
    temp = int(t.split(':')[0])
    if m=='pm' and temp!=12:
        temp+=12
        return str(temp)+':'+str(t.split(':')[1])+':00'
    else:
        return t+':00'


def check_valid_time(tm):
    if int(tm.split(':')[0]) >=24:
        return False
    else:
        return True

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    diary = load_workbook('ReminderDiary.xlsx')['Sheet1'].values
    next(diary)
    df = pd.DataFrame(data=diary,columns=('time','am/pm','task','status'))
    del diary
    for index, row in df.iterrows():
        if row['time'] == None:
            break
        try:
            a_time = clean_time(row['time'].strftime('%H:%M:%S'),row['am/pm'])
            if not(check_valid_time(a_time)):
                continue
            current_time = datetime.now().strftime('%H:%M:%S')
            tdelta = datetime.strptime(a_time, '%H:%M:%S') - datetime.strptime(current_time, '%H:%M:%S')
            del current_time
            tdelta = str(tdelta).split(':')
            secs = int(int(tdelta[0])*3600+int(tdelta[1])*60+int(tdelta[2]))
            del tdelta,a_time
            time.sleep(secs)
            notification.notify(
                title=row['task'],
                app_icon="D:\Github Projects\Basic-Python-Projects\Task_Reminder\img\Task_Reminder.ico",
                message='Hey ayush its time to complete your following task... '+row['task'],
                timeout=3,
            )
            time.sleep(1)
            speak('Hey ayush its time to complete your task named '+row['task'])

        except Exception as e:
            print('There is some error in your scheduling')
            print(e)
    print('Its end of your schedule. Have a great day ahead')