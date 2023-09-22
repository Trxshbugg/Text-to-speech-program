import pyttsx3
import speech_recognition as sr
from pyttsx3 import voice
from win32com.server import exception

engine = pyttsx3.init('sapi5')  #speech api jarvis le bolne tone ya stored huncha
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCmd():
    r = sr.Recognizer()  #recog lai call gar-ya
    with sr.Microphone() as source:
        print('I\'m listening..')
        r.pause_threshold = 1  #1 sec samma bolena vane ni wait garcha sunna
        audio = r.listen(source)

    try:
        print("Recognizing the voice..")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said :{query}\n")

    except exception as e:
        print("Could you please repeat that again.. ")
        return "none"
    return query

if __name__ == "__main__":
    while True:
        query = takeCmd().lower()
        if 'jarvis' in query:
            print("Hi baby!")
            speak("Hi baby!")



