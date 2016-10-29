import wave
import sys
import numpy as np
from pydub import AudioSegment
from pydub.silence import split_on_silence
from scipy.io import wavfile as wav
from scipy.fftpack import fft



# FORMAT = 8
# CHANNELS = 1 #2
# RATE = 44100
# CHUNK = 1024
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "file.wav"
 
# audio = pyaudio.PyAudio()
 
# # start Recording
# stream = audio.open(format=FORMAT, channels=CHANNELS,
#                 rate=RATE, input=True,
#                 frames_per_buffer=CHUNK)
# print "recording..."
# frames = []
 
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
# print "finished recording"
 
 
# stop Recording
# stream.stop_stream()
# stream.close()
# audio.terminate()
 
# waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# waveFile.setnchannels(CHANNELS)
# waveFile.setsampwidth(audio.get_sample_size(FORMAT))
# waveFile.setframerate(RATE)
# waveFile.writeframes(b''.join(frames))
# waveFile.close


sound_file = AudioSegment.from_wav("file.wav")
audio_chunks = split_on_silence(sound_file, 
    # must be silent for at least half a second
    min_silence_len=300,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-16
)

def dataFourier(time_slot, fourier_slots):
	fft_time_slot = fft(time_slot)
	d = len(fft_time_slot) / 2
	fft_time_slot = abs(fft_time_slot[d, :], 'r')
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


for i, chunk in enumerate(audio_chunks):
    out_file = "./chunk{0}.wav".format(i)
    print "exporting", out_file
    chunk.export(out_file, format="wav")	

# for i in enumerate(audio_chunks):
# 	rate, data = wav.read('chunk{0}.wav'.format(i))
# 	print "DATALENGTH: ", len(data)
	data = [(ele/2**8.)*2-1 for ele in data]
# 	time_values = ','.join(dataTimeDivandFourier(data, 300, 10))
