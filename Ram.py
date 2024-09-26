import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import time
import wikipedia
import webbrowser
import os
import pyautogui
import random

from pygame import mixer



from INTRO import play_gif
play_gif


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        
        return "None"
    return query
             
def alarm(query):
    timehere =open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                
                    #go to sleep Mode
                if "go to sleep" in query:
                    speak("Ok sir , You can  call me anytime")
                       
                        #change Password
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")


                        #calculate
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("Ram","")
                    Calc(query)

               

                

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                      file = open("tasks.txt","w")
                      file.write(f"")
                      file.close()
                      no_tasks = int(input("Enter the no. of tasks :- "))
                      i = 0
                      for i in range(no_tasks):
                         tasks.append(input("Enter the task :- "))
                         file = open("tasks.txt","a")
                         file.write(f"{i}. {tasks[i]}\n")
                         file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                           tasks.append(input("Enter the task :- "))
                           file = open("tasks.txt","a")
                           file.write(f"{i}. {tasks[i]}\n")
                           file.close()

                
                
                elif "play a game" in query:
                       from game import game_play
                       game_play()
               

                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

              


               
                    #conversation

                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")  


                elif "stop" in query:
                     pyautogui.press("k")
                     speak("video stop")
                elif "play" in query:
                     pyautogui.press("k")
                     speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")

                elif "volume up" in query:
                    from keyboar import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboar import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
           
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                if 'wikipedia' in query:
                   speak('Searching Wikipedia...')
                   query = query.replace("wikipedia", "")
                   results = wikipedia.summary(query, sentences=2)
                   speak("According to Wikipedia")
                   print(results)
                   speak(results)
                elif 'open youtube' in query:
                     webbrowser.open(f"https://www.youtube.com/search?q={query.replace(' open youtube', '').strip()}")
                     time.sleep(5)
            
                elif 'open google' in query:
                     webbrowser.open(f"https://www.google.com/search?q={query.replace('  google', '').strip()}")
                     time.sleep(5)
       
                elif "temperature" in query:
                    search = "temperature in karwar"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "weather in karwar"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

      
                elif "the time" in query:
                     strTime = datetime.datetime.now().strftime("%H %M")
                     speak(f"sir the time is{strTime}")

                elif "set an alarm" in query:
                    print("input time example:- 10:10:10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")


                elif "finally sleep"in query:
                    speak("going to sleep,sir")
                    exit()
    
                
                elif "remember that" in query:
                     rememberMessage = query.replace("remember that","")
                     rememberMessage = query.replace("Ram","")
                     speak("You told me to "+  rememberMessage)
                     remember = open("Remember.txt","a")
                     remember.write(rememberMessage)
                     remember.close()
                elif "what do you remember" in query:
                     remember = open("Remember.txt","r")
                     speak("You told me to remember " + remember.read())
                
               
               
               
                elif "shutdown the system" in query:
                     shutdown = speak("shutdowning Sir")
                     os.system("shutdown /s /t 1")

                     
        
                     
                    
                      

                



                

                
    

             

    



