# // first we'll wirte speak feature  
# // we'll import a module

import pyttsx3
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[1].id)

#   //we will pass the argument and it will speak that
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi, I am Jarvis, designed by Scientist Venkatesh Ranjan Verma. Please tell me how may I help you")

if __name__ == "__main__":
    # speak("venkatesh ranjan verma is a good boy")
    wishMe()