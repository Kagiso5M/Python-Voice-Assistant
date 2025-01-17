#Author: Kagiso Peter Motsisi
#Domain: Python Programming
#Project: 2
#----------------------------------------------------------------------------------------------------------
import speech_recognition as sr #install 1st(pip cmd)
import datetime
import subprocess
import pywhatkit #install 1st (pip cmd)
import pyttsx3 #install 1st (pip cmd)
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)#voice[0] for a male voice
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Removing sound distortions and unwanted noice")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..but it would be nice if you greet first')
        recordedaudio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))
    except Exception as ex:
        print(ex)

    if 'hello'in text:
        a='Hello, how may I help you?..'
        engine.say(a)
        engine.runAndWait()
    if 'make commands' in text:
        b='Okay, I am all ears, make your commands..'
        engine.say(b)
        engine.runAndWait()
    if 'browser'in text:
        c='Opening browser..'
        engine.say(c)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    if 'time'in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'linkedIn'in text:
        d='opening linkedIn..'
        engine.say(d)
        engine.runAndWait()
        webbrowser.open('www.linkedin.com/in/kagiso-motsisi-54529b152')
    if 'youtube'in text:
        e='opening youtube..'
        engine.say(e)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
while True:
    cmd()