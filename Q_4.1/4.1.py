#!/usr/bin/env python
# coding: utf-8

import numpy as np
from scipy.signal import fftconvolve, firwin, lfilter, butter
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd

def visualizar_audio(audio_filtrado, nome): 
    
    # Visualizando a forma de onda com o eco
    fig = plt.figure(figsize=(14, 10))
    plt.subplot(211)
    librosa.display.waveplot(audio_filtrado, sr=sr)
    plt.title(nome)
    
    plt.subplot(212)
    # Visualizando o spectro da onda com o eco
    X = librosa.stft(audio_filtrado)
    Xdb = librosa.amplitude_to_db(abs(X))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.title("Espectro")
    
    fig.savefig(nome + '.png')

audio , sr = librosa.load('car1.wav')

visualizar_audio(audio, "audio_original")

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

lowcut = 2000.0
highcut = 7000.0

audio_filtrado = butter_bandpass_filter(audio, lowcut, highcut, sr, order=6)
visualizar_audio(audio_filtrado, "audio_filtrado")
librosa.output.write_wav('audio_filtrado.wav', audio_filtrado, sr)


# https://dsp.stackexchange.com/questions/55768/remove-background-noise-from-audio-file-python-or-matlab
# 
# https://www.mathworks.com/help/matlab/ref/fft.html#buuutyt-9