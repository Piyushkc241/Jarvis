import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi=""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com") 
    elif c.lower().startswith("play"):
        song=c.lower().split(' ')[1]    
        webbrowser.open(musicLibrary.music[song])
    elif "news"  in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
            # parsing
            data=r.json()

            # extract the artciles
            articles=data.get('articles',[])

            for article in articles:
                speak(article['title'])

    
if __name__=="__main__":
    speak("Initializing Jarvis.....")

    while True:
    # listen for  the wake word "jarvis"

        r=sr.Recognizer()
        
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)
                

        except Exception as e:
            print("Error; {0}".format(e))

