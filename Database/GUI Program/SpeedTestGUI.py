
import pyttsx3

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


def run_uit():
    Speak("I am Checking Sir, Wait for a while")
    print("Analyzing...")
    import speedtest
    speed = speedtest.Speedtest()
    upload = speed.upload()
    upload_speed = round(upload/(10**6),2)
    download = speed.download()
    download_speed = round(download/(10**6),2)
    
    Speak(f"Downloading Speed is {upload_speed} Mb per second And Uploading Speed is {download_speed} Mb per second")
    exit()

run_uit()
