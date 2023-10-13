# Penggunaan Low pass filter

import numpy as nu
from scipy.signal import butter, lfilter, freqz 
import matplotlib.pyplot as p


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

print("Nama: Dhea Tirta Ananta")
print("NRP: 5009201142")

# Filter yang digunakan
order = 10
freq = 30.0       #sampling rate
cutoff = 1  #frekuensi cutoff filter

# Koefisien filter
b, a = butter_lowpass(cutoff, freq, order)

# Plot respon frekuensi 
w, h = freqz(b, a, worN=4000)
p.subplot(2, 1, 1)
p.plot(0.5*freq*w/nu.pi, nu.abs(h), 'r')
p.plot(cutoff, 0.5*nu.sqrt(2), 'ko')
p.axvline(cutoff, color='k')
p.xlim(0, 0.5*freq)
p.title("Respon Frekuensi Lowpass")
p.xlabel('Frekuensi Sinyal + Noise dan Sinyal Hasil Filter [Hz]')
p.grid()


# Input sinyal yang akan difilter
T = 5.0            
n = int(T * freq)     # jumlah sampel
t = nu.linspace(0, T, n, endpoint=False)
# Sinyal noise yang ditambahkan 
data = nu.sin(2*nu.pi*t) + 1.5*nu.cos(10*nu.pi*t)+2*nu.cos(12*nu.pi*t)
# Aplikasikan filter dan plot sinyal sebelum dan sesudah difilter
y = butter_lowpass_filter(data, cutoff, freq, order)

p.subplot(2, 1, 2)
p.plot(t, data, 'r-', label='Sinyal+Noise')
p.plot(t, y, 'g-', linewidth=2, label='Sinyal Hasil ilter')
p.xlabel('Waktu(s)')
p.grid()
p.legend()

p.subplots_adjust(hspace=0.5)
p.show()
