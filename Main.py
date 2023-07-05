# Speak Function :- How to use Voices
import pyttsx3
from gtts import gTTS #Google assistant voice
from playsound import playsound
import speech_recognition as sr;
from keyboard import press
from keyboard import write
from keyboard import press_and_release
import webbrowser as web


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

def Speak_Assis(audio):
    kk = gTTS(audio)
    kk.save("Assis.mp3")
    playsound("Assis.mp3")
# playsound("D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\Sounds\\song.mp3")

# playsound("D:\\SSD Files\\Program\\PythonProgram\\Personal Assistant\\Database\\Voices\\Raveena\\Raveena.mp3")

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
    
    # op = open('Data.txt','rb')
    # op.write(f"{query}")
    # op.close()

    return query.lower()

def TakeCommand_Hindi():
    r = sr.Recognizer() #Start listening from microphone
    with sr.Microphone() as source:
        print(":) Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        print(":) Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f"=> Your Command: {query}\n " )
    except:
        return ""
    Speak_Assis(query)
    return query.lower()

# TakeCommand()
# TakeCommand_Hindi()

def TaskExecute():
    while True:
        query = TakeCommand()
        if 'search on youtube' in query:
            Query = query.replace("jarvis", "")
            query = Query.replace("search on youtube","")
            from Features import YouTubeSearch
            YouTubeSearch(query)
        elif 'search on google' in query:
            from Features import GoogleSearch
            GoogleSearch(query)
        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)
        elif 'download' in query:
            from Features import DownloadYTVideo
            DownloadYTVideo()
        elif 'download this playlist' in query:
            from Features import PlaylistDownload
            PlaylistDownload()
        elif 'speed' in query:
            from Features import SpeedTest
            SpeedTest();
        elif 'calculate' in query:
            from Features import Calculator
            Calculator(query);
        elif 'whatsapp message' in query:
            name = query.replace("jarvis ", "")
            name = name.replace("send whatsapp message to ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"What is the Message for {Name}")
            msg  = TakeCommand()
            from Automation import WhatsAppMsg
            WhatsAppMsg(Name,msg)
        elif 'call' in query:
            name = query.replace("jarvis ", "")
            name = query.replace("now ", "")
            name = name.replace("call ","")
            name = name.replace("to ","")
            name = name.replace("the ","")
            Name = str(name)
            Speak(f"Sure Sir, Calling to {Name}")
            from Automation import WhatsAppCall
            WhatsAppCall(Name)

        elif 'open new tab' in query:
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
        elif 'space news' in query:
            Speak("Sure Sir, please tell me date?")
            Date = TakeCommand() # YYYY-MM-DD
            date1 = Date.replace("and", "-")
            date2 = date1.replace("zero", "0")
            date3 = date2.replace(" ", "")

            from Nasa_Api import NasaNews
            NasaNews(date3)
        elif 'my location' in query:
            from Features import MyLocation
            MyLocation()
        elif 'where is' in query:
            from Automation import GoogleMap
            Place = query.replace("where is ", "")
            Place = Place.replace("jarvis", "")
            GoogleMap(Place)
        elif 'write a note' in query:
            from Automation import Notepad
            Notepad()
        elif 'close notepad' in query:
            from Automation import CloseNotePad
            CloseNotePad()
        else:
            from Database.Chatbot.Chatbot import ChatterBot
            reply = ChatterBot(query)
            Speak(reply)
            if 'bye' in query:
                break
            elif 'exit' in query:
                break
            elif 'go' in query:
                break
 


TaskExecute() 


