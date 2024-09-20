
# --------------- Text Translator program --------------

import pyttsx3 # for text to speech
import speech_recognition as sr
from googletrans import Translator


speak=pyttsx3.init() # initialized text to speech
speak.setProperty('rate',160) # speed of the robo speech
voice = speak.getProperty('voices') # getting system build voices

# robo speaking code
def robo(message):
    speak.say(message)
    speak.runAndWait()

# asking for change the voice to  male or female
print("Note : if you choose write something else or nothing it's by default male voice")
voice_type=input("please enter the type of voice male or female ? : ")
if(voice_type=="female" or voice_type =="Female"):
    speak.setProperty('voice',voice[1].id)

def listen():
    r=sr.Recognizer() #initialize  voice recognizer
    t=Translator() #initialize text translator
    with sr.Microphone() as source : # taking input from your system microphon
        while True: # aking continue this question
            print("say want you want : ")
            audio=r.listen(source, phrase_time_limit=6)
            try:
                text=r.recognize_google(audio,language ='hi-IN') # using google API for audio recognizing
                print("you said :",text) #printing audio into text which we stor in text variable
                transalted = t.translate(text, src='hi',dest='en')
                print("translate (English) :", transalted.text)
                robo(transalted.text)
            except:
                print("sorry i am unable to understand you ")

if __name__=="__main__":
    listen()
    
    
    


