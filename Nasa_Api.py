import requests
import webbrowser as web
import pyttsx3

Api_Key = "Z0RNhlkD89CTmi5rQH5VblagSlG2UtmXvzStCHpo"





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

def NasaNews(Date):
    Speak(f"Here is the important news for date {Date}")
    Url = "https://api.nasa.gov/planetary/apod?api_key="+ str(Api_Key)
    Params = {'date':str(Date)}
    r = requests.get(Url,params=Params)
    data = r.json()
    
    Info = data['explanation']
    Title = data['title']
    Image_url = data['url']
    web.open(Image_url)
    Speak(f"Title : {Title}")
    Speak(f"According to Nasa : {Info}")

