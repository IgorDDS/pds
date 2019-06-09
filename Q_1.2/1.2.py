#!/usr/bin/env python
# coding: utf-8

# Links:
# 
# ---
# 
# https://musicinformationretrieval.com/ipython_audio.html
# 
# https://scipy-cookbook.readthedocs.io/items/ApplyFIRFilter.html
# 
# ---

# get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from scipy.signal import fftconvolve, firwin, lfilter
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
    
# Carrega o arquivo de audio como um array numpy
# e retorna também sua taxa de amostragem
audio , sr = librosa.load('sp04.wav')

# Criando o eco
# O taxa de amostragem aqui é 22050, e portanto D = 500 deixa o eco menos percepitivel
D = 500 # atraso definido no enunciado
eco = np.zeros(len(audio) + D)
for i in range(len(audio)):
    eco[i+D] = audio[i]

# Adicionando o eco no audio
audio_com_eco = 0.5*eco
for i in range(len(audio)):
    audio_com_eco[i] += audio[i]

librosa.output.write_wav('audio_com_eco.wav', audio_com_eco, sr)

# Definindo a função de transferencia
num = [1] # numeradorda função de transferencia
den = np.zeros(D + 1) # denominador da função de transferencia
den[0] = 1


# aplica o filtro no audio com eco

a = 0.5 #primeiro teste
den[D] = -a

audio_filtrado_a_menos05 = lfilter(num, den, audio_com_eco)
librosa.output.write_wav('audio_filtrado_a_menos_0.5.wav', audio_filtrado_a_menos05, sr)

visualizar_audio(audio_filtrado_a_menos05 , 'audio_filtrado_a_menos_0.5')

a = 0.9 #segundo teste
den[D] = -a

# aplica o filtro no audio com eco
audio_filtrado_a_menos09 = lfilter(num, den, audio_com_eco)
librosa.output.write_wav('audio_filtrado_a_menos_0.9.wav', audio_filtrado_a_menos09, sr)

visualizar_audio(audio_filtrado_a_menos09 , 'audio_filtrado_a_menos_0.9')


a = 0.25 #terceiro teste
den[D] = -a

# aplica o filtro no audio com eco
audio_filtrado_a_menos025 = lfilter(num, den, audio_com_eco)
librosa.output.write_wav('audio_filtrado_a_menos_0.25.wav', audio_filtrado_a_menos025, sr)

visualizar_audio(audio_filtrado_a_menos025 ,'audio_filtrado_a_menos_0.25')


a = 0.5 #quarto teste
den[D] = a

# aplica o filtro no audio com eco
audio_filtrado_a_mais05 = lfilter(num, den, audio_com_eco)
librosa.output.write_wav('audio_filtrado_a_mais_0.5.wav', audio_filtrado_a_mais05, sr)

visualizar_audio(audio_filtrado_a_mais05 ,'audio_filtrado_a_mais_0.5')

a = 0.9 #quinto teste
den[D] = a

# aplica o filtro no audio com eco
audio_filtrado_a_mais09 = lfilter(num, den, audio_com_eco)
librosa.output.write_wav('audio_filtrado_a_mais_0.9.wav', audio_filtrado_a_mais09, sr)

visualizar_audio(audio_filtrado_a_mais09 ,'audio_filtrado_a_mais_0.9')


a = 0.25 #sexto teste
den[D] = a

# aplica o filtro no audio com eco
audio_filtrado_a_mais025 = lfilter(num, den, audio_com_eco)
librosa.output.write_wav('audio_filtrado_a_mais_0.25.wav', audio_filtrado_a_mais025, sr)

visualizar_audio(audio_filtrado_a_mais025 ,'audio_filtrado_a_mais_0.25')

