# ARTIFICIAL INTELLENGCE USING PYTHON PROGRAMMING

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning boss!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon boss")

    else:
        speak("Good Evening boss")

    speak("I am jarvis. we are online and ready.")
    speak("The weather outside in ahmedabad is 32°C with scattered clouds" )


def takecommand():
    # it takes microphone input from the user and returns back string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching sir...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to my knowledge")
            print(results)
            speak(results)

        elif 'open google' in query:

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("http://www.google.com")

        elif 'open youtube' in query:

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("http://www.youtube.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'play music' in query:
            music_dir = 'C:\\my songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open telegram' in query:
            telegramPath = "C:\\Users\\BHARAT NEGI\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(telegramPath)

        elif 'hello jarvis' in query:
            speak("hello sir, how was your day.")

        elif 'who created you' in query:
            speak("mr.saksham negi created me")

        elif 'open instagram' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(
                'https://www.instagram.com/direct/inbox/')

        elif 'play calm music' in query:
            speak("sure sir")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(
                'https://music.youtube.com/watch?v=N2AE4EEzGSk&list=RDAMVMN2AE4EEzGSk')

        elif 'play that song i like to listen while working' in query:
            speak("Sir, i think i know what to play ")
            music_dir = 'C:\\savage song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "good night" in query:
            speak("Good night sir, have a good dream")
            exit()
