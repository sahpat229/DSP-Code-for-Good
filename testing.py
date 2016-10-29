from scipy.io import wavfile as wav
from scipy.fftpack import fft
from urllib import urlretrieve
import numpy as np
import speech_recognition as sr
import re
import requests
import json
import fileinput

#getting string in form of 

#getting real string input

lines = split('&', input)
realinput = split(' ', realstring)
autism_arr = []
real_arr = []
fingerprintsarr = []
for line in lines:
		fields = split('|', line)
		autism = fields[0]
		real = fields[2]
		fingerprints = int(split(',', real))
		autism_arr.append(autism)
		real_arr.append(real)
		fingerprintsarr.append(fingerprints);

for realstring in realinput:
	if realstring not in autism_arr:
		filename = realstring + ".wav"
		urlretrieve("http://api.voicerss.org/?key=04f49802d32d442ca997d4d2ea76d3d5"
	        "&hl=en-us&c=wav&src="+realstring, filename)
	    rate, data = wav.read(filename)
	
