
import pyttsx3
import wikipedia
import webbrowser as web
import pywhatkit
import speech_recognition as sr
from pywikihow import WikiHow, search_wikihow
import os
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)
engine.setProperty('rate', 170)


def Speak(audio):
    print("     ")
    print(f":) {audio}")
    print("     ")
    engine.say(audio)
    engine.runAndWait()

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak(" This is What I found for your search: ")
    pywhatkit.playonyt(term)
    Speak(" This May also help you Sir")

def GoogleSearch(term):
    query1 = str(term)
    query = query1.replace('search on google',"")
    query = query.replace("jarvis ","")
    query = query.replace("what is ","")
    # query = query.replace("how to ","")
    query = query.replace("who is ","")
    query = query.replace("what do you mean by ","")
    query = query.replace("explain me ","")
    query = query.replace("tell me ","")

    Speak("This is what i found on google")

    Query = str(query)
    # pywhatkit.search(Query)

    if 'how to' in Query:
        Query = Query.replace("how to ","")
        pywhatkit.search(Query)
        max_result =1
        how_to_func = search_wikihow(query=Query, max_results=max_result)
        assert len(how_to_func) == 1
        # how_to_func[0].print()
        Speak(how_to_func[0].summary)
    else:
        pywhatkit.search(Query)
        search = wikipedia.summary(Query,sentences=2)
        Speak(f" According to your search: {search}")

def Alarm(query):
    TimeHere = open("D:\\SSD Files\Program\\PythonProgram\\Personal Assistant\Database\\Data.txt",'a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\ExtraFeatures\\Alarm.py")

def DownloadYTVideo():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    hotkey('alt','d')

    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value)
    def Download(link):
        url = YouTube(link)
        video = url.streams.get_by_resolution("720p")
        video.download("D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\Youtube Video\\")

    Download(Link)
    Speak("Done Sir, Video Downloaded in Youtube Video Folder")
    Speak("You can Go and Check it Out")
    os.startfile("D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\Youtube Video\\")

def PlaylistDownload():
    from pytube import Playlist
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep
    sleep(2)
    click(x=406, y=48)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value)
    def DownloadP(link):
        url = Playlist(link)
        for video in url.videos:
            video.streams.get_by_resolution("720p")
            video.download("D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\Youtube Video\\")

    DownloadP(Link)
    Speak("Done Sir, Playlist Downloaded in Youtube Video Folder")
    Speak("You can Go and Check it Out")
    os.startfile("D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\Youtube Video\\")

def SpeedTest():
    os.startfile("D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\GUI Program\\SpeedTestGUI.py")

def Calculator(query):
    query = str(query)
    query = query.replace("jarvis","")
    query = query.replace("calculate","")
    query = query.replace("multiply","*")
    query = query.replace("multiplied","*")
    query = query.replace("x","*")
    query = query.replace("plus","+")
    query = query.replace("minus","-")
    query = query.replace("into","*")
    query = query.replace("divide","/")
    query = query.replace("divide by","/")
    query = query.replace("modulo","%")
    query = query.replace("module","%")
    query = query.replace("modules","%")
    Speak(f"The answer is {eval(query)}")

def MyLocation():
    Speak("Checking...")
    ip_add = requests.get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + ip_add + ".json"
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    op = f"https://www.google.com/maps/place/{state}+{country}" 
    web.open(op)
    Speak(f"Sir, You are now in {state, country}.")


    
