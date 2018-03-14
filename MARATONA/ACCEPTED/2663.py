N = int(raw_input())
K = int(raw_input())

results = []

for i in range(N):
    results.append(int(raw_input()))

count = 0
last = -1
for value in reversed(sorted(results)):
    if count < K or last == value:
        count += 1
        last = value
    else:
        break

print count
