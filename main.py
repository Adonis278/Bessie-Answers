import json

import requests
import speech_recognition as sr
# from time import ctime
# import time
# import os
# from gtts import gTTS
# import requests, json
# import pyaudio
import pyttsx3

"""def listen():
   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("I am listening...")
       audio = r.listen(source)
   data = ""
   try:
       data = r.recognize_google(audio)
       print("You said: " + data)
   except sr.UnknownValueError:
       print("Google Speech Recognition did not understand audio")
   except sr.RequestError as e:
       print("Request Failed; {0}".format(e))
   return data


def respond(audioString):
   print(audioString)
   tts = gTTS(text=audioString, lang='en')
   tts.save("speech.mp3")
   os.system("mpg321 speech.mp3")


def digital_assistant(data):
   if "how are you" in data:
       listening = True
       respond("I am well")

   if "what time is it" in data:
       listening = True
       respond(ctime())

   if "stop listening" in data:
       listening = False
       print('Listening stopped')
       return listening
   return listening


s = listen()

digital_assistant(s)"""
r = sr.Recognizer()


def SpeakText(command):
    voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    engine.setProperty('rate', 140)
    engine.say(command)
    engine.runAndWait()


with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0.3)
    SpeakText("Hi, my name is Bessie, how may I help you?")


"""def click(s):
    try:
        text = r.recognize_google(s)
        text = text.lower()
        selector(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
        SpeakText("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
        SpeakText("Request Failed; {0}".format(e))"""


def operate(t):
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.25)
            print('....')
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                text = text.lower()
                selector(text)
            except sr.UnknownValueError:
                print("Google Speech Recognition did not understand audio")
                SpeakText("Google Speech Recognition did not understand audio")
                break
            except sr.RequestError as e:
                print("Request Failed; {0}".format(e))
                SpeakText("Request Failed; {0}".format(e))
                break


def selector(d):
    if 'change' or 'switch' in d:
        change()
    elif 'reservation' or 'book' in d:
        book()


def change():
    response = requests.get('/flights?date=YYYY-MM-DD&destination=GSO').text
    response_info = json.loads(response)
    flight_list = []
    for flight_info in response_info['flightNumber']:
        flight_list.append([flight_info['flightNumber'], flight_info['city']])


def book():
    SpeakText("May I please have your First name?")


"""with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0.1)

    print('I am listening....')

    audio2 = r.listen(source2)

    '''text = r.recognize_google(audio2)
    text = text.lower()

    print('Did you say ' + text)
    SpeakText(text)"""
print('start')

"""
def speak():
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.3)
        SpeakText("Hi, my name is Bessie, how may I help you?")

        print('I am listening....')

        audio2 = r.listen(source2)
    try:
        text = r.recognize_google(audio2)
        text = text.lower()
        if 'book' or 'reservation' in text:
            t = 'I understand you want to make a reservation, I can help you with the whole process. May I please have'\
                'your name?'
            SpeakText(t)
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.3)

                print('I am listening....')
                audio2 = r.listen(source2)
            try:
                text = r.recognize_google(audio2)
                text = text.lower()
                SpeakText("Thank you " + text)
                SpeakText("Where will you fly from?")
                with sr.Microphone() as source3:
                    r.adjust_for_ambient_noise(source3, duration=0.3)

                    print('I am listening....')
                    audio3 = r.listen(source3)
                    te = r.recognize_google(audio2)
                    te = te.lower()
                    SpeakText("thank you. What is your destination?")
                    with sr.Microphone() as source4:
                        r.adjust_for_ambient_noise(source4, duration=0.3)

                        print('I am listening....')
                        audio4 = r.listen(source4)
                        text = r.recognize_google(audio4)
                        print(text.lower())
                        SpeakText('Please confirm the details:' +
                                  'Flying from Charlotte to Dallas')
 
            except sr.UnknownValueError:
                print("Google Speech Recognition did not understand audio")
                SpeakText("Google Speech Recognition did not understand audio")
            except sr.RequestError as e:
                print("Request Failed; {0}".format(e))
                SpeakText("Request Failed; {0}".format(e))
        elif 'charlotte' in text:
            SpeakText("thank you. What is your destination?")
            speak()
        elif 'dallas' in text:
            SpeakText('Please confirm these details')

        # print(text)
        # SpeakText(text)
     except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
speak() """
operate()
print('Done')
