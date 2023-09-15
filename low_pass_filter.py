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
# Filter requirements.
order = 10
freq = 30.0       # sample rate, Hz
cutoff = 3.667  # desired cutoff frequency of the filter, Hz

# Get the filter coefficients so we can check its frequency response.
b, a = butter_lowpass(cutoff, freq, order)

# Plot the frequency response.
w, h = freqz(b, a, worN=8000)
p.subplot(2, 1, 1)
p.plot(0.5*freq*w/nu.pi, nu.abs(h), 'r')
p.plot(cutoff, 0.5*nu.sqrt(2), 'ko')
p.axvline(cutoff, color='k')
p.xlim(0, 0.5*freq)
p.title("Lowpass Filter Frequency Response")
p.xlabel('Frequency [Hz]')
p.grid()


# Demonstrate the use of the filter.
# First make some data to be filtered.
T = 5.0             # seconds
n = int(T * freq)     # total number of samples
t = nu.linspace(0, T, n, endpoint=False)
# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
data = nu.sin(2*nu.pi*t) + 1.5*nu.cos(10*nu.pi*t)+2*nu.cos(12*nu.pi*t)
# Filter the data, and plot both the original and filtered signals.
y = butter_lowpass_filter(data, cutoff, freq, order)

p.subplot(2, 1, 2)
p.plot(t, data, 'r-', label='Sinyal+Noise')
p.plot(t, y, 'g-', linewidth=2, label='Sinyal Hasil ilter')
p.xlabel('Waktu(sec)')
p.grid()
p.legend()

p.subplots_adjust(hspace=0.35)
p.show()
