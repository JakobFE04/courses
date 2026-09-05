import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


# Working script to play tones sampled from a cosine!

F_S1 = 4000
F_S2 = 1500
F = 1000
F_PLAYBACK = 44100

t_total = 1

N1 = np.arange(0, t_total, 1/F_S1)
N2 = np.arange(0, t_total, 1/F_S2)

def x_func(t):
    return np.array(np.cos(2 * np.pi * F * t))


x1 = x_func(N1)
x1_play = np.repeat(x1, int(F_PLAYBACK/F_S1))
x2 = x_func(N2)
x2_play = np.repeat(x2, int(F_PLAYBACK/F_S2))


sd.default.device = 7
sd.play(x2_play, samplerate=F_PLAYBACK)
sd.wait()


