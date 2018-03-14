import matplotlib.pyplot as plt
import scipy.fftpack
import numpy as np

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode = 'same')
    return y_smooth

flux = []
latency = []

with open('flux', 'r') as f:
    for word in f.read().split():
        flux.append(int(word))


with open('latencies', 'r') as f:
    for word in f.read().split():
        latency.append(float(word))

f = np.asarray(flux)
l = np.asarray(latency)

plt.plot(sorted(f), sorted(l))
plt.xlabel("Flux")
plt.ylabel("Latency")
plt.show()
