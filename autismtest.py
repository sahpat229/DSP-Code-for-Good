#!/usr/bin/env python3

import speech_recognition as sr
import re
import requests
import json
import fileinput

from os import path
from difflib import SequenceMatcher

files = []

for line in fileinput.input():
    files.append(line)


AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), files[0])

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    autismoinput = re.sub("[^\w]", " ", r.recognize_google(audio)).split()
    output = []
    train = dict()
    lines = open(files[1]).read().splitlines()
    for line in lines:
        words = line.split('&')
        train[word[0]] = word[1]
    headers = { "X-Mashape-Key": "IpoJf4zXvAmshlkkbGjK0heE1N03p1AgXXvjsnvFC5cbLgshi7",  "Accept": "application/json" }
    for word in autismoinput:
        if (train.get(word) != 'None'):
            output.append(train.get(word))
        else:
            r1 = requests.get(' https://wordsapiv1.p.mashape.com/words/' + word + '/pronunciation', params = headers)
            r1.json()
            maxratio = 0.0
            outputstring = ""
            for key, value in train.items():

                r2 = requests.get(' https://wordsapiv1.p.mashape.com/words/' + key + '/pronunciation', params = headers)
                r2.json()
                if (SequenceMatcher(None, r1["pronunciation"]["all"], r2["pronunciation"]["all"]).ratio() > maxratio):
                    maxratio = SequenceMatcher(None, r1["pronunciation"]["all"], r2["pronunciation"]["all"]).ratio()
                    outputstring = value
            output.append(outputstring)
    shalin = ""
    for word in output:
        shalin += word + '&' 
    print (shalin)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

