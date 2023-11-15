import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import soundfile as sf
import scipy

# Un semnal sinusoidal de frecventa 800 Hz, care sa dureze 3 secunde.
frequency = 800
duration = 3
t = np.linspace(0.0, duration, int(duration / 0.0001))
amplitude = 1.0  
signal = amplitude * np.sin(2 * np.pi * frequency * t)

sd.play(signal, 44100)

sf.write("ex3.wav", signal, 44100)

signal_2 = scipy.io.wavfile.read("signal.wav")
