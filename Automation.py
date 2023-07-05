from keyboard import press
from keyboard import write
from keyboard import press_and_release
import pyttsx3
import speech_recognition as sr;
import webbrowser as web
from time import sleep
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import datetime
import pyautogui
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate', 170)

def Speak(audio):
    print("     ")
    print(f":) {audio}")
    print("     ")
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer() #Start listening from microphone
    with sr.Microphone() as source:
        print(":) Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        print(":) Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"=> Your Command: {query}\n " )
    except:
        return ""
  
    return query.lower()

def ChromeAuto(command):
    while True:
        query = str(command)
        if 'open new tab' in query:
            press_and_release('ctrl+t')
        elif 'close tab' in query:
            press_and_release('ctrl+w')
        elif 'open new window' in query:
            press_and_release('ctrl+n')
        elif 'open history' in query:
            press_and_release('ctrl+h')
        elif 'open download' in query:
            press_and_release('ctrl+j')
        elif 'open bookmark' in query:
            press_and_release('ctrl+d')
            press('enter')
        elif 'open incognito' in query:
            press_and_release('Ctrl+Shift+n')
        elif 'switch tab' in query:
            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to","")
            num = Tab
            bb = f'ctrl + {num}'
            press_and_release(bb)
        elif 'open' in query:
            name = query.replace("open","")
            NameA =str(name)
            if 'youtube' in NameA:
                web.open("https://www.youtube.com/")
            elif 'instagram' in NameA:
                web.open("https://www.instagram.com/")
            elif 'leetcode' in NameA:
                web.open("https://leetcode.com/problemset/all/")
            elif 'gfg' in NameA:
                web.open("https://practice.geeksforgeeks.org/")
            else:
                string = "https://www." + NameA
                string1 = string.replace(" ","")
                web.open(string1)

def WhatsAppMsg(name,message):
    press_and_release('ctrl+esc') 
    sleep(3)
    write("WhatsApp")
    sleep(1)
    press("enter")
    sleep(10)
    write(name)
    sleep(2)
    press('tab')
    sleep(1)
    press("enter")

    sleep(1)
    write(message)
    sleep(2)
    press('enter')

def WhatsAppCall(name):
    press_and_release('ctrl+esc') 
    sleep(3)
    write("WhatsApp")
    sleep(1)
    press("enter")
    sleep(10)

    write(name)
    sleep(2)
    press('tab')
    sleep(1)
    press("enter")
    sleep(1)

    press_and_release('ctrl+shift+f') 
    sleep(0.5)
    press_and_release('shift+tab')
    sleep(0.5) 
    press_and_release('shift+tab') 
    press_and_release('shift+tab')
    sleep(2) 
    pyautogui.press('enter')

def YouTubeAuto(command):
    query = str(command)
    if 'pause' in query:
        press('space bar')
    elif 'resume' in query:
        press('space bar')
    elif 'full screen' in query:
        press('f')
    elif 'film screen' in query:
        press('t')
    elif 'skip' in query:
        press('l')
    elif 'back' in query:
        press('j')
    elif 'increase speed' in query:
        press_and_release('shift+.')
    elif 'decrease speed' in query:
        press_and_release('shift+,')
    elif 'previous' in query:
        press_and_release('shift+p')
    elif 'next' in query:
        press_and_release('shift+n')
    elif 'search' in query:
        press('/')
        Speak("What to search Sir?")
        search = TakeCommand()
        write(search)
        sleep(1)
        press('enter')
    elif 'mute' in query:
        press('m')
    elif 'unmute' in query:
        press('m')
    else:
        Speak("Command not Recognized, try again")

def GoogleMap(Place):
    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(Place,addressdetails=True)
    target_latlong = location.latitude,location.longitude
    location = location.raw['address']
    target = {'city' : location.get('city',''),
              'state' : location.get('state',''),
              'country' : location.get('country','')}
    current_loc = geocoder.ip('me')
    current_latlong = current_loc.latlng
    distance = str(great_circle(current_latlong,target_latlong))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance), 2)

    web.open(url=Url_Place)

    Speak(target)
    Speak(f"Sir, {Place} is {distance} Kilometer Away from your location")

def Notepad():
    Speak("Tell me the Query? I Am Ready To Write")
    writes = TakeCommand()
    time = datetime.datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"
    with open(filename, "w") as file:
        file.write(writes)
    path_1 = "D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\" +str(filename)

    path_2 = "D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\Notepad\\" +str(filename)
    os.rename(path_1,path_2)
    os.startfile(path_2)

def CloseNotePad():
    os.system("TASKKILL /F /im Notepad.exe")

# WhatsAppMsg("BLS", "Hi BLS, This is the testing message of Automated jarvis (Kindly ignore this)")
# WhatsAppCall("Naveen Jain")