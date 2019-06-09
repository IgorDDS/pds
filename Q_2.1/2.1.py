#!/usr/bin/env python
# coding: utf-8

# https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
# 
# https://dsp.stackexchange.com/questions/49620/how-to-classify-a-kernel-as-low-pass-filter-lpf-or-high-pass-filter-hpf-how
# 

import numpy as np
from scipy import signal
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

imagem = Image.open("lena_rings.bmp")


imagem_filtrada = imagem.filter(ImageFilter.GaussianBlur(1.3))

imagem_filtrada.save('blur_gaussiano_2.1.bmp')

# meu_kernel_gaussiano = ImageFilter.Kernel(
#     size=(3, 3),
#     kernel=filtro_gaussiano(),
#     scale=sum(filtro_gaussiano()),  # default
#     offset=0  # default
#     )


# imagem_filtrada = imagem.ImageFilter.kernel(meu_kernel_gaussiano)

# imagem_np = np.array(imagem)

# imagem_filtrada = signal.fftconvolve(imagem_np, filtro_gaussiano(sigma = 5), mode='full')
# # Image.fromarray(pix)
# imagem_pra_salvar = Image.fromarray(imagem_filtrada)
# imagem_pra_salvar = imagem_pra_salvar.convert("L")
# imagem_pra_salvar.save("fftconvolve.bmp")