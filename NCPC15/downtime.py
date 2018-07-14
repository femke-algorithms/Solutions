from math import ceil

n, m = [int(i) for i in input().split()]

r = [int(input()) for _ in range(n)]

h = 0

for i, t in enumerate(r):
    c = h
    if i - c >= 0 and t - r[i - c] < 1000:
        c += 1
        while i - c >= 0 and t - r[i - c] < 1000:
            c += 1
        h = c

print(ceil(h / m))
