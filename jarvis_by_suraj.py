import replace
import webbrowser
import os
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3 #text to speech conversion module
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)

"""def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',o)
    server.ehlo()
    server.strttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()"""

def speak(audia):
    engine.say(audia)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("good morning !!!")
    elif hour >= 12 and hour <=6:
        speak("good after noon!")
    else:
        speak("good evening !")
    speak("I am  Jariv Sir. Please tell me ,how can i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    
#try is used where where we think thta it will raise an error or expectance is hig error raising !!!!!!!
    try:
        print("recognising......")
        query = r.recognize_google(audio, language = 'en-hin')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please.....")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'Wikipedia' in query:
            speak("searching Wikipedia....")
            toSearch = takeCommand()
            result=wikipedia.summary(toSearch,sentences=2)
            speak("according to wikipidea")
            print(result)
            speak(result) 
            print("srry")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir='D:\\Non critical\\songs\\favorite songs2'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,song[0]))
        elif 'time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(f"the time is {strTime}")
        
        elif 'open vs code'in query :
            codePath = "C:\\Users\\suraj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        
        """elif 'send email to suraj ' in query:
            try:
                speak("What should i send to suraj")
                content = takeCommand()
                to = "09surajmaurya@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to send the email your freind suraj beccause of some error!")
            """