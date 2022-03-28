from tkinter import *
from PIL import Image, ImageTk
import threading
import os
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import time
import ctypes
import re
from Sound import Sound
from Keyboard import Keyboard

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
        print("listening...")
        btn.insert(INSERT, "listening...\n")
        btn.see(END)
        r.energy_threshold = 1000  # minimum audio energy to consider for recording
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        btn.insert(INSERT, "Recognizing...\n")
        btn.see(END)
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        btn.insert(INSERT, f"user said: {query}\n")
        btn.see(END)

    except Exception as e:
        print(e)

        print("say that again please")
        btn.insert(INSERT, "say that again please\n")
        btn.see(END)
        speak("say that again please")
        return "None"
    return query

def toggleplay():
    global is_paused
    is_paused=False

def togglepause():
    global is_paused
    is_paused=True

def play(): 
    while True:
        
        if not is_paused:

        # if 1:
            query = takeCommand().lower()

            if 'mute' in query :
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

        else:
            print("Not execute")
            btn.insert(INSERT, "Not execute\n")
            btn.see(END)
            break

count = 0

def shiftImage(event):
        
    if count % 2 == 0:
        canvas1.itemconfig(button, image=stopImage)
        print("clicked at play")
        toggleplay()
        threading.Thread(target=play).start()

    else:
        canvas1.itemconfig(button, image=playImage)
        print("clicked at stop")
        togglepause()

    globals()['count'] += 1

#make a tk window 
root = Tk()
root.title('')
root.resizable(width=False, height=False)
root.geometry('900x500')

#photo
icon1 = Image.open("playbutton.png")
reicon1 = icon1.resize((100, 100))
icon2 = Image.open("pausebutton.png")
reicon2 = icon2.resize((100, 100))
logo = Image.open("logo5.png")
relogo = logo.resize((150, 100))
bg = PhotoImage(file = "bgimage.png")
playImage = ImageTk.PhotoImage(reicon1)
stopImage = ImageTk.PhotoImage(reicon2)
exitImage = PhotoImage(file="exit.png")
LogoImage = ImageTk.PhotoImage(relogo) 

#make canvas window 
canvas1 = Canvas(width=900, height=500)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,
					anchor = "nw")

#make button
button = canvas1.create_image(380, 60, anchor=NW, image=playImage)
canvas1.tag_bind(button, "<Button-1>", shiftImage)

#logo
logo = canvas1.create_image(45, 60, anchor=NW, image=LogoImage)
#make text box
# Button with black border
border = LabelFrame(canvas1, bd = 6, bg = "black")
canvas1.create_window(50, 200, window=border, anchor="nw")

btn = Text(border, width = 50, height=10,bd=5,
            bg="#083C49", fg = "black", font=("Times New Roman", 12) )
btn.pack()

#entry1 = Text(canvas1, width=100, height=20, bd=10, bg="#083C49") 
#canvas1.create_window(50, 280, window=entry1, anchor="nw")

#make haedaing
canvas1.create_text(250, 110, text= "Media Player", font=("Times New Roman", 30), fill="white")

is_paused = False

def close():
    togglepause()
    root.destroy()

#make exit button
button2 = Button(canvas1, image=exitImage, command=close)
canvas1.create_window(205, 435, window=button2, anchor="nw")
#threading.Thread(target=close).start()

root.mainloop()
