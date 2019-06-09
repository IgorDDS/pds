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

audio , sr = librosa.load('teste_de_som.wav')

visualizar_audio(audio,  'teste_de_som')

audio = audio*30

f =  466.16 # Frequencia do ruido

t = np.arange(len(audio)) # tempo em amostras
# compute the value (amplitude) of the sin wave at the for each sample
ruido = np.sin(2*np.pi*f * (t/sr)) 

audio_com_ruido = audio + ruido
librosa.output.write_wav('audio_com_ruido.wav', audio_com_ruido, sr)
visualizar_audio(audio_com_ruido,  'audio_com_ruido')


# ### Vou fliltrar o sinal com um filtro butterworth passa banda usando a ideia de telefonias
# ### pegando a parte mais importante pra compreenção da voz humana entre 4KHz e 8Khz 
# 
# https://scipy-cookbook.readthedocs.io/items/ButterworthBandpass.html
# 
# https://www.dpamicrophones.com/mic-university/facts-about-speech-intelligibility

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
highcut = 4000.0

audio_filtrado = butter_bandpass_filter(audio_com_ruido, lowcut, highcut, sr, order=6)
librosa.output.write_wav('audio_filtrado.wav', audio_filtrado, sr)
visualizar_audio(audio_filtrado,  'audio_filtrado')

# filtro_fir = firwin(6, [lowcut,highcut], pass_zero=False, fs = sr)

# audio_filtrado_fir = fftconvolve(audio_final, filtro_fir[np.newaxis, :], mode='valid')
# audio_filtrado_fir = lfilter(filtro_fir, [1.0], audio_final)

# ipd.Audio(audio_filtrado_fir, rate=sr) # o audio ficou ruizinho mas o ruido foi eliminado

