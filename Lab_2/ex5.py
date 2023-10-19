import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import soundfile as sf

duration = 5
frequency_1 = 200
frequency_2 = 400

t = np.linspace(0.0, duration, int(duration / 0.0001))

amplitude = 1.0  
signal_1 = amplitude * np.sin(2 * np.pi * frequency_1 * t)
signal_2 = amplitude * np.sin(2 * np.pi * frequency_2 * t)

final_signal = np.concatenate((signal_1, signal_2))

sd.play(final_signal, 44100)
sf.write("ex5.wav", final_signal, 44100)

# Atunci cand creste frecventa semnalului, sunetul devine mai ascutit

