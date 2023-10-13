# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 22:10:05 2023

@author: ASUS
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:02:09 2023

@author: ASUS
"""

from matplotlib import pyplot as plt
from math import cos, sin, pi, log
import matplotlib.cm as cm

#buat sinyal persegi yang akan dilakukan Fourier Transform
print("Nama : Dhea Tirta Ananta")
print("NRP : 5009201142")
print("Tugas 2 FFT")
def sinyal_pers(A, B):
    
    bagian_kiri = [1 for i in range(A*1)]
    sinyal_kiri0 = [0 for i in range(10)]
    sisi_tengah = [1]
    bagian_kanan = bagian_kiri[:]
    sinyal_kanan0 = sinyal_kiri0[:]
    sinyal = sinyal_kiri0+bagian_kiri+sisi_tengah+bagian_kanan+sinyal_kanan0
    plt.subplot(2, 1, 1)
    plt.stem(list(range(-(10+1*A), (10+1*A)+1)), sinyal, 'b', markerfmt='o', basefmt='b')
    return sinyal

def dft(xn):
    c = 0
    N = len(xn)
    x_k = [x for x in range(N)]
    for k, nilai_x_k in enumerate(x_k):
        for n, nilai_x_n in enumerate(xn):
            c1 = nilai_x_n*(cos(2*pi*k*n/N)-1j*sin(2*pi*k*n/N))
            c += c1
            c1 = 0
        x_k[k] = c
        c = 0
    tengah = [abs(i) for i in x_k]
    limit_tengah = N//2
    tengah = tengah[:limit_tengah]
    tengah = [2*i for i in tengah]
    norm = [i/N for i in tengah]
    #pencerminannn
    cermin_norm= norm[:]
    cermin_norm.reverse()
    x_base = list(range(len(norm)))
    cermin_x_base = x_base[:]
    cermin_x_base.reverse()
    cermin_x_base = [-1*i for i in cermin_x_base]
    plt.subplot(2, 1, 2)
    plt.stem(x_base, norm, 'b', markerfmt='o', basefmt='b')
    plt.stem(cermin_x_base, cermin_norm, 'b', markerfmt='o', basefmt='b')
    plt.show()
    return norm+cermin_norm   

#input sinyal yang akan di fft dengan batas bawah (-A) dan batas atas yang sama (A)
#membuat sinyal 2D

def filteringft(sigx, sigy, xp, yp):
    gambar = bikingambar (len(xp), len(yp))
    for i in range(len(yp)):
        for j in range(len(yp)):
            gambar[i][j] = xp[i]*yp[j]
    plt.subplot(1, 2, 2)
    plt.imshow(gambar, origin='lower', extent=(0, len(xp), 0, len(yp)),
        cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    gambar = bikingambar(len(xp), len(yp))
    for i in range(len(yp)):
        for j in range(len(xp)):
            gambar[i][j] = sigx[i]*sigy[j]
    plt.subplot(1, 2, 1)
    plt.imshow(gambar, origin='lower', extent=(0, len(xp), 0, len(yp)),
        cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    plt.show()

def bikingambar(xp, yp):
    gambar = []
    for i in range(yp):
        x_colors = []
        for j in range(xp):
            x_colors.append(0)
        gambar.append(x_colors)
    return gambar

sigx = sinyal_pers(0.5, 0.5) #sinyal hasil ft pada sumbu x
sigy = sinyal_pers(0.5, 0.5) #sinyal hasil ft sumbu y

DFTx = dft(sigx) #DFT pada sumbu x
DFTy = dft(sigy) #DFT pada sumbu y

filreringfft(sigx, sigy, DFTx, DFTy)