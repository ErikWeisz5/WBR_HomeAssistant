import pyttsx3  # module to allow to speak
import speech_recognition as sr  # text to speak module
import wikipedia
import datetime
import webbrowser
import smtplib


print("Initializing WBR...")

MASTER = 'Nick'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# speak function will pronounce the string which is passed out
def speak(text):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning' + MASTER)
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon' + MASTER)
    else:
        speak('Good Afternoon' + MASTER)

    speak('I am WBR... How may I help you?')


# this command takes command from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am listening...')
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, Language='en')
        print(f"user said: {query}\n")


    except Exception as e:
         print('say that again please')
         return query

# main command starts here
speak('Greetings... Im Wilhelmina Beatrice Rahner (WBR)')
wishMe()
query = takeCommand()

# logic for executing tasks
if 'wikipedia' in query.lower(): # wuery lower as it detect voice as lower case
        speak('Searching wikipedia..')
        query = query.replace('wikipedia',"")
        results = wikipedia.summary(query, sentences =2)
        speak(results)
elif 'open youtube' in query.lower():
       url = "youtube.com" # specifi curl used
       chrome_path.get(chrome_path).open(url)

       #add play music
#elif 'play music' in query.lower():
        #songs = os.listdir("")