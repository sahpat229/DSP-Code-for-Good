from scipy.io import wavfile as wav
from scipy.fftpack import fft
from urllib import urlretrieve
import numpy as np
import matplotlib.pyplot as plt
import sys
import re
import speech_recognition as sr


r = sr.Recognizer()
with sr.AudioFile('Recording.wav') as source:
	audio = r.record(source)

try:
	autisminput = ""
	autism_input = re.sub("[^\w]", " ", r.recognize_google(audio)).split()
	for word in autism_input:
		autisminput += word
    	autisminput += "\t"
   	autisminput = autisminput[:len(autisminput)]		

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
#received autisminput, parentinput

#autisminput = split(' ', autisminput)
#parentinput = split(' ', parentinput)


def dataFourier(time_slot, fourier_slots):
	fft_time_slot = fft(time_slot)
	d = len(fft_time_slot) / 2
	fft_time_slot = abs(fft_time_slot[d:])
	#plt.plot(fft_time_slot, 'r')
	#plt.show()
	counter_2 = 0
	fourier_skip = len(fft_time_slot) / fourier_slots
	fourier_values = []
	for j in range(fourier_slots):
		if j == (fourier_slots - 1):
			temp_data = fft_time_slot[counter_2:]
			fourier_values.append(max(temp_data))
		else:
			temp_data = fft_time_slot[counter_2:counter_2 + fourier_skip]
			counter_2 += fourier_skip
			fourier_values.append(max(temp_data))
	return fourier_values


def dataTimeDivandFourier(data, time_slots, fourier_slots):
	data = [(ele/2**8.)*2-1 for ele in data]
	data_slots = len(data) / time_slots
	counter =0
	time_values = []
	for i in range(time_slots):
		if i == (time_slots - 1):
			new_data = data[counter:]
			time_values.append(dataFourier(new_data, fourier_slots))
		else:
			new_data = data[counter:counter+data_slots]
			counter += data_slots
			time_values.append(dataFourier(new_data, fourier_slots))
	return time_values


def populateData():
	autisminput = ["Hell", "Am", "Goo"]
	parentinput = ["Hello", "A", "Good"]

	if (len(autisminput) != len(parentinput)):
		sys.exit()

	#get wav input of text to speech

	dtft_output = ""

	for i in range(len(autisminput)):
		item = autisminput[i]
		dtft_output = dtft_output + item + "|"
		filename = item+".wav"
		urlretrieve("http://api.voicerss.org/?key=04f49802d32d442ca997d4d2ea76d3d5&hl=en-us&c=wav&src="+item, filename)
		rate, data = wav.read(filename)
		realitem = parentinput[i]
		timefingers = dataTimeDivandFourier(data, 300, 10)
		#print "TIMEFINGERS:", timefingers
		for arr in timefingers:
			for item in arr:
				dtft_output += str(item)
				dtft_output += ","
		dtft_output = dtft_output[:len(dtft_output) - 1]
		dtft_output += "|"
		dtft_output += realitem
		dtft_output += "&"

	return dtft_output[:len(dtft_output) - 1]



