# // first we'll wirte speak feature ,   ....., install wikipedia module
# // we'll import a module

import pyttsx3                                    # module ko instal karo lo with the help of pip    
import datetime
import speechRecognition as sr                    # me is module ko sr naam se use karunga
import wikipedia                                  # pip install wikipedia


engine = pyttsx3.init('sapi5')                    #speech api, we are using it here to take the inbuilt voice of my window system
voices = engine.getProperty('voices')             #we'll get 2 voices, male voice anf female voice
# print(voices[0].id) -> david and zira
engine.setProperty('voice',voices[0].id)




#   //we will pass the argument and it will speak that
def speak(audio):                                  
    engine.say(audio)
    engine.runAndWait()




def wishMe():                                        #mere ko wish karega, based on the time
    hour = int(datetime.datetime.now().hour)         #datetime module install karna padega
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi, I am Jarvis, always ready for your Service Sir ")




def takeCommand():                                      #This func. will the input from system microphone
   
    r = sr.Recognizer()                                  #This class will help in recognizing the the audio from system microphone
    with sr.Microphone() as source:                      # isko me source microphone ke liye use karunga
        print ("Listening...")                          # ye is liye lika taki user ko pata chal jai ki system soon raha he
        r.pause_threshold =1                            # it takes seconds of non-speaking audio before a phase is complete, jo ki by default 0.8 second hota he, maltlab mere ko 1 sec. ka time de do means me 1 sec. ka gap le lu to system us phase tak input complete na samagh le
        audio = r.listen(source)                        # audio recognition module ka he
#                                                       aap energy_threshold increase kar do to minimise te outside disterbance

    try:
        print("Recognition...")                          #try ham tab likhte he jab hame lagta he error aa sakta he
        query = r.recognize_google(audio, language='en-in')      #recognize bing bhi likh saktr he             en-in: english india
        print("User said:", query)                        # or could be written as f string ie    print(f"User said: {query}\n) 
    #                                                      yaha tak audio recognise karaai gai he

    except Exception as e:
        #print(e)                                   aap ne kuch google func ko boola or vo recognaize nahi kar paya, tab control except vale block me aaiga, and app us error ko print kar sakte he, ya fir say that again bole 
        print("Say that again please....")
        return "None"                               #none string return kardega jab koi problem aa jaati he

    return query                                    # finally me return kara doonga the input that I've given to microphone



if __name__ == "__main__":                          # main function
    # speak("venkatesh ranjan verma is a good boy")
    wishMe()
 #   takeCommand()       

    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based in the query
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia","")            #it will remove the wikipedia word from the string
            results= wikipedia.summary(query,sentence=2)     #it will read 2 lines from the the                     