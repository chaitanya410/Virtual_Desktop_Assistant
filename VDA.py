from datetime import datetime
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType

  

def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()



ui,_ = loadUiType("VDA.ui")

class MainApp(QMainWindow,ui):
      def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.speakButton.clicked.connect(wishMe())






if __name__=="__main__":
    main()

 
engine =pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good Morning!")
    elif hour >=12  and hour<18:
        speak("Good Afternoon!")
    else:
        speak("good evening!")
    speak("I am vishnu,Please tell me how may i help you :")


def takeCommand():
    
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("recongnizing...")
        query=r.recognize_google(audio,language="en-in")
        print("User said:" ,query)
    except Exception as e:
       # print(e)
        print("say that again please...")
        return "None"
    return query  
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
      
        #logic for executing task based on query
      
        if "wikipedia" in query:
           speak("searching Wikipedia...")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open edge" in query:
            webbrowser.open("edge.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open spotify" in query:
            webbrowser.open("spotify.com")
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"the time is {strTime}")
        elif "open code" in query:
            code_path="D:\chaitu\vs code\Microsoft VS Code\Code.exe"
            os.startfile(code_path)
     
