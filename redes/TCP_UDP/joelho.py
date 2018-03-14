import matplotlib.pyplot as plt

flux = []
latency = []

with open('flux', 'r') as f:
    for word in f.read().split():
        print word
        #flux.append(int(word))


with open('latencies', 'r') as f:
    for word in f.read().split():
        print word
        #latency.append(int(word))

print(len(flux), len(latency))

t = zip(flux, latency)

plt.plot(sorted(t))
plt.xlabel('Flow')
plt.ylabel('Latency')
plt.show()
