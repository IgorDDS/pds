#!/usr/bin/env python
# coding: utf-8

# ## Projeto de PDS 2019.1
# Igor Dias da Silva

# ---
# #### Questão 1.1
# 
#  Utilizando janelamento, crie um filtro FIR passa alta com as seguintes especificações:
#  
#  ωs = 0.6π, ωp = 0.75π; As = 50 dB
# 
# Justifique todas as suas decisões de projeto. 

import numpy as np                  
from scipy import signal,special     
import matplotlib.pyplot as plt     

# Dados da questão
Ws = 0.3*np.pi
Wp = 0.2*np.pi
As = 50

Wc = (Ws + Wp)/2

delta_W = np.abs(Wp - Ws)

# Expressão pega da tabela para As =  50
beta = 0.5842*(As - 21)**0.4 + 0.07886*(As - 21) 

M = int(np.ceil(((As - 7.95)/(14.36*delta_W/(2*np.pi))+1)) + 1)

# Essa função projeta o filtro com a janela especificada
# Para o caso da janela de kaiser é preciso informar beta
filtro = signal.firwin(M, Wc/np.pi, window=('kaiser', beta))
fig = plt.figure(1)
plt.stem(filtro)
fig.savefig('filtro.png')

w, h = signal.freqz(filtro)
fig = plt.figure(2)
plt.title('Resposta do filtro na frequencia')
ax1 = fig.add_subplot(111)
plt.plot(w/np.pi, 20 * np.log10(abs(h)), 'b')
plt.plot(w/np.pi , np.full(len(w), -50) , 'r')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Freq [rad/amostra]')

fig.savefig('resposta_filtro.png')