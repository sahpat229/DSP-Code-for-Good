#!/usr/bin/env python3

import speech_recognition as sr
import re

from os import path
#Get wav and train json from Shalin
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    autismoinput = re.sub("[^\w]", " ", r.recognize_google(audio)).split()
    count  = len(autismoinput)
    output = []
    for word in autismoinput:
        if (train.get(word) != 'None'):
            output.append(train.get(word))
        else:
            output.append(word)
    #Pass to Shalin
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
