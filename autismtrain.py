#!/usr/bin/env python3

import speech_recognition as sr
import re

from os import path
import fileinput

files = []

for line in fileinput.input():
    files.append(line)

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), files[0])

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    autismoinput = re.sub("[^\w]", " ", r.recognize_google(audio)).split()
    count  = len(autismoinput)
    s_autismoinput = str(count) + ','
    for word in autismoinput:
        shalin += word + '&' 
    print (shalin)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
