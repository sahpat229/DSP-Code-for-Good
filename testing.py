from scipy.io import wavfile as wav
from scipy.fftpack import fft
from urllib import urlretrieve
import numpy as np
#import speech_recognition as sr
import re
import requests
import json
import fileinput

#getting string in form of 

#getting real string input

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


def getOutputs(inputstring, realstring):
	lines = re.split('&', inputstring)
	autisminput = re.split(' ', realstring)
	autism_arr = []
	real_arr = []
	fingerprintsarr = []
	for line in lines:
		fields = re.split('\|', line)
		autism = fields[0]
		real = fields[2]
		fingerprints = map(float, (re.split(',', fields[1])))
		autism_arr.append(autism)
		real_arr.append(real)
		fingerprintsarr.append(fingerprints);

	print real_arr

	string_outputs = []

	for autismstring in autisminput:
		if autismstring not in autism_arr:
			filename = autismstring + ".wav"
			urlretrieve("http://api.voicerss.org/?key=04f49802d32d442ca997d4d2ea76d3d5&hl=en-us&c=wav&src="+autismstring, filename)
			rate, data = wav.read(filename)
			realfingers = dataTimeDivandFourier(data, 300, 10)
			realfingers2 = []
			for guy in realfingers:
				for guy2 in guy:
					realfingers2.append(guy2)
			minimumind = -1
			minimum = 10000000000
			for index in range(len(fingerprintsarr)):
				arr = fingerprintsarr[index]
				if len(arr) == len(realfingers2):
					print "NICE"
				suma = 0
				for index2 in range(len(arr)):
					# print realfingers2[index2]
					# print arr[index2]
					suma += abs(realfingers2[index2] - arr[index2])
				if suma < minimum:
					minimum = suma
					minimumind = index
			string_outputs.append(real_arr[minimumind])
		else:
			return real_arr[autism_arr.index(autismstring)]
	return string_outputs

	# for autismstring in autisminput:
	# 	if autismstring not in autism_arr:
	# 		filename = autismstring + ".wav"
	# 		urlretrieve("http://api.voicerss.org/?key=04f49802d32d442ca997d4d2ea76d3d5&hl=en-us&c=wav&src="+autismstring, filename)
	# 		rate, data = wav.read(filename)
	# 		realfingers = dataTimeDivandFourier(data, 300, 10)
	# 		minimum_index = -1
	# 		minimum = 10000000000

	# 		counter = 0
	# 		index = 0
	# 		while (counter < 10) and (index < 3000):
	# 			all_sums = []
	# 			for index2 in range(len(fingerprintsarr)):
	# 				for []


	# 		for index in range(len(fingerprintsarr)):
	# 			arr = fingerprintsarr[index]
	# 			while (index2 < len(arr)):
	# 				counter = 0
	# 				suma = 0
	# 				while (counter < 300) and (index2 < len(arr)):

	# 				suma += abs(realfingers[index2] - arr[index2])
	# 			if suma < minimum:
	# 				minimum = suma
	# 				minimumind = index
	# 	else:
	# 		return real_arr[autism_arr.index(autismstring)]