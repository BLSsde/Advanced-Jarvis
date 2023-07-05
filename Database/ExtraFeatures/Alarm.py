import os
from playsound import playsound
import datetime


# playsound("D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\ExtraFeatures\\alarmsound.mp3")
extracted_time = open("D:\\SSD Files\Program\\PythonProgram\\Personal Assistant\Database\\Data.txt",'rt')
time = extracted_time.read()
Time = str(time)
delete_time = open("D:\\SSD Files\Program\\PythonProgram\\Personal Assistant\Database\\Data.txt",'r+')
delete_time.truncate(0)
delete_time.close()

def RingNow(time):
    time_to_set = str(time)
    time_now = time_to_set.replace("jarvis","")
    time_now = time_now.replace("set alarm for","")
    time_now = time_now.replace("set alarm for me at","")
    time_now = time_now.replace("set alarm for me","")
    time_now = time_now.replace("create alarm for me at","")
    time_now = time_now.replace("alarm for","")
    time_now = time_now.replace("0 ","0")
    time_now = time_now.replace("zero ","0")
    time_now = time_now.replace(" and ",":")

    Alarm_Time = str(time_now)
    
    Alarm_Time = str(time_now).strip()
    print(Alarm_Time)
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == Alarm_Time:
            print("Wake Up Sir, It's Time To Work",current_time)
            playsound("D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\ExtraFeatures\\alarmsound.mp3")
        elif current_time>Alarm_Time:
            print("It's break now")
            break

RingNow(Time)


