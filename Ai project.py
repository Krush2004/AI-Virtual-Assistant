import pyttsx3
import speech_recognition 
import datetime
import pywhatkit
import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
import time
from time import sleep
import os 
import pyautogui
from pynput.keyboard import Key,Controller
import wolframalpha
import json
import speedtest
from fnmatch import translate
from time import sleep
import googletrans
from googletrans import Translator,LANGUAGES
from gtts import gTTS
from playsound import playsound
import time
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from textblob import TextBlob


for i in range(3):
    a = input("Enter Password to open Ema :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
        
def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")

    speak("Please tell me, How can I help you ?")

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

def summarize_text_sumy(text):
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 3)  # Summarize to 3 sentences
        return ' '.join([str(sentence) for sentence in summary])
    except Exception as e:
        print(f"An error occurred while summarizing text: {e}")
        return "Sorry, I couldn't summarize the text."

def summarize_text_input():
    text = get_text_input()
    summary = summarize_text_sumy(text)
    speak("Here is the summary: " + summary)

def get_text_input():
    print("Please type your input text:")
    user_input = input()  # Get text input from the user
    return user_input

def correct_text(text):
    try:
        blob = TextBlob(text)
        corrected_text = blob.correct()
        return str(corrected_text)
    except Exception as e:
        print(f"An error occurred while correcting text: {e}")
        return "Sorry, I couldn't correct the text."

def correct_text_input():
    text = get_text_input()
    corrected_text = correct_text(text)
    print("Original Text: " + text)
    print("Corrected Text: " + corrected_text)
    speak("Here is the corrected text: " + corrected_text)
    
def translategl(query):
    speak("SURE SIR")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")   
    text_to_translate = translator.translate(query,src = "auto",dest= b,)
    text = text_to_translate.text
    try : 
        speakgl = gTTS(text=text, lang=b, slow= False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        
        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("Unable to translate")

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("ema","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("ema","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")


def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("ema","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)
        
        
dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("ema","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                
                
keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)
        
        
def WolfRamAlpha(query):
    apikey = "5R49J7-J888YX9J2V"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("ema","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=a83b73039b244c9794d137187257591b",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=a83b73039b244c9794d137187257591b",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=a83b73039b244c9794d137187257591b",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=a83b73039b244c9794d137187257591b",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=a83b73039b244c9794d137187257591b",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a83b73039b244c9794d137187257591b"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")
        
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
                
                elif "hello ema" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                    
                elif "google" in query:
                    searchGoogle(query)
                elif "youtube" in query:
                    searchYoutube(query)
                elif "wikipedia" in query:
                    searchWikipedia(query) 
                elif "temperature" in query:
                      search = "temperature in delhi"
                      url = f"https://www.google.com/search?q={search}"
                      r  = requests.get(url)
                      data = BeautifulSoup(r.text,"html.parser")
                      temp = data.find("div", class_ = "BNeawe").text
                      speak(f"current{search} is {temp}")
                elif "weather" in query:
                      search = "temperature in delhi"
                      url = f"https://www.google.com/search?q={search}"
                      r  = requests.get(url)
                      data = BeautifulSoup(r.text,"html.parser")
                      temp = data.find("div", class_ = "BNeawe").text
                      speak(f"current{search} is {temp}")
                      
                elif "the time" in query:
                      strTime = datetime.datetime.now().strftime("%H:%M")    
                      speak(f"Sir, the time is {strTime}")
                      
                elif "open" in query:
                      openappweb(query)
                elif "close" in query:
                      closeappweb(query)
                      
                elif "pause" in query:
                       pyautogui.press("k")
                       speak("video paused")
                elif "play" in query:
                       pyautogui.press("k")
                       speak("video played")
                elif "mute" in query:
                       pyautogui.press("m")
                       speak("video muted")
                elif "volume up" in query:
                      speak("Turning volume up,sir")
                      volumeup()
                elif "volume down" in query:
                      speak("Turning volume down, sir")
                      volumedown()
                      
                elif "remember that" in query:
                      rememberMessage = query.replace("remember that","")
                      rememberMessage = query.replace("ema","")
                      speak("You told me "+rememberMessage)
                      remember = open("Remember.txt","a")
                      remember.write(rememberMessage)
                      remember.close()
                elif "what do you remember" in query:
                      remember = open("Remember.txt","r")
                      speak("You told me " + remember.read())
                      
                elif "calculate" in query:
                      query = query.replace("calculate","")
                      query = query.replace("ema","")
                      Calc(query)
                      
                elif "translate" in query:
                    query = query.replace("ema","")
                    query = query.replace("translate","")
                    translategl(query)      
                
                elif "news" in query:
                      latestnews()
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                    
                elif "summary it" in query:
                    summarize_text_input()
                    
                elif "correct text" in query:
                    correct_text_input()
                    
                elif "screenshot" in query:
                     im = pyautogui.screenshot()
                     im.save("ScreenShort.jpg")
                     
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                      
                elif "finally sleep" in query:
                     speak("Going to sleep,sir")
                     exit()
