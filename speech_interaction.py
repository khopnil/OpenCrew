import logging
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from stenocmplt import stenoeng

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetings():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        print("Good morning.")
        speak("Good morning.")
    elif 12 <= hour < 18:
        print("Good afternoon.")
        speak("Good afternoon.")
    else:
        print("Good evening.")
        speak("Good evening.")

    print("How may I help you sir?")
    speak("How may I help you sir?")


def command():
    """
    it takes mic input and
    :return: string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-bn')
        print(f"- {query}\n")

    except Exception as e:
        logging.exception(e)
        print("Sorry I didn't catch that. Say it again please.")
        return "None"
    return query


def m_indx():
    music_dir = 'D:\\Music'
    mlist = []
    counter = 0
    for f in os.listdir(music_dir):
        if f.endswith(".mp3"):
            mlist.append(f)
            counter += 1
    print(f"{counter} tracks found.\n")
    return mlist


def m_indxp():
    music_dir = 'D:\\Music'
    mplist = []
    counter = 0
    for f in os.listdir(music_dir):
        if f.endswith(".mp3"):
            mplist.append(os.path.join(music_dir, f))
            counter += 1
    return mplist[random.randint(0, counter)]


if __name__ == '__main__':
    greetings()
    while True:
        query = command().lower()
        # command()

        if 'wikipedia' in query:
            speak("Searching Wikipedia.")
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia, ")
            print(result)
            speak(result)

        elif 'hello' in query:
            speak("Hello sir. How may I help you?")

        elif 'youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'spotify' in query:
            os.startfile('C:\\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.199.878.0_x86__zpdnekdrzrea0\Spotify.exe')
        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'full form' in query:
            speak("Since I'm not sure of what shorthand you have just asked for, can you kindly type it out "
                  "below?")
            print("Please type below:")
            inp = str(input())
            res = stenoeng(inp)
            speak(f"{inp} stands for {res}")

        elif 'music' in query:
            print(m_indx())
            speak("Do you want me to play something from here?")
            confrm = command().lower()
            if 'yes' in confrm:
                speak("Sure. Here you go.")
                os.startfile(m_indxp())
            elif 'no' or 'cancel' in confrm:
                speak("As you wish.")
                pass
            else:
                break

        elif "your name" in query:
            speak("My name is Sigrun. And I am a part of the project OpenCrew.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I : %M %p")
            print(strTime)
            speak(f"It's {strTime} right now.")

        elif 'stop' or 'shutdown' in query:
            print("Alright.")
            speak("Alright.")
            break

        else:
            break











