import pyttsx3 
import speech_recognition as sr
import time
import ctypes
from Keyboard import Keyboard 
from Sound import Sound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def play():

    while True:

        query = takeCommand().lower()


        if 'mute' in query:
            Sound.mute()

        elif 'volume up' in query:
            Sound.volume_up()
    
        elif 'volume down' in query:
            Sound.volume_down()
        
        elif 'set volume minimum' in query:
            Sound.volume_min()

        elif 'set volume maximum' in query:
            Sound.volume_max()

        elif 'set volume ' in query:
            x = query.split()
            print (x[2])
            result = int(x[2])
            Sound.volume_set(result)

        elif 'back' in query or 'backward' in query:
            Keyboard.keyDown(0x12)
            Keyboard.keyDown(0x25)
            Keyboard.keyUp(0x25)
            Keyboard.keyUp(0x12)

        elif 'forward' in query:
            Keyboard.keyDown(0x12)
            Keyboard.keyDown(0x27)
            Keyboard.keyUp(0x27)
            Keyboard.keyUp(0x12)
    
        elif 'play' in query or 'pause' in query:
            Keyboard.keyDown(0xB3)
            Keyboard.keyUp(0xB3 )
    
