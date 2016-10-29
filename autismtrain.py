#!/usr/bin/env python3

import speech_recognition as sr
import re

from os import path
#Get wav from Shalin
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test2.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    #autismoinput = re.sub("[^\w]", " ", r.recognize_google(audio)).split()
    count  = len(autismoinput)
    #Send count to shalin
    #wait for response from shalin
    #if shalin says its ok, he provides parentinput
    train = dict(zip(autismoinput, parentinput))
    #Pass to Shalin
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
