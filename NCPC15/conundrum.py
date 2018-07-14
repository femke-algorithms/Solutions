s = input().upper()

d = 'PER'
i, n = 0, 0

while i < len(s):
    if s[i] == d[i % 3]:
        n += 1
    i += 1

print(len(s) - n) 