import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import time
import ctypes
import re
from Sound import Sound
from Keyboard import Keyboard
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("lisning.......")
        r.energy_threshold = 1000  # minimum audio energy to consider for recording
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")


    except Exception as e:
        print(e)

        print("say that again please")
        speak("say that again please")
        return "None"
    return query


def play(): 
    while True:
        # if 1:
        query = takeCommand().lower()

        if 'mute' in query or 'chup' in query or 'chup kar' in query or 'shant' in query or 'shant ho ja' in query or 'set up' in query:
            Sound.mute()

        elif 'unmute' in query:
            Sound.mute()

        elif 'volume up' in query:
            Sound.volume_up()

        elif 'volume down' in query:
            Sound.volume_down()

        elif 'set volume minimum' in query:
            Sound.volume_min()

        elif 'set volume maximum' in query:
            Sound.volume_max()

        elif 'play' in query or 'pause' in query:
            Keyboard.keyDown(0x20)
            Keyboard.keyUp(0x20)

        elif 'backward' in query:
            Keyboard.keyDown(0x25)
            Keyboard.keyUp(0x25)

        elif 'forward' in query:
            Keyboard.keyDown(0xA7)
            Keyboard.keyUp(0xA7)

        elif 'set volume' in query:
            string1 = query
            volume = int(re.search(r'\d+', string1).group())
            print(volume)
            Sound.volume_set(volume)

