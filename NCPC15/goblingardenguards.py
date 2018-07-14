l = []

n = int(input())

def find_start(l, v):
    

for x, y in [[int(i) for i in input().split()] for _ in range(n)]:
    l.append((x, y))

a = sorted(l, key=lambda x: x[0])
b = sorted(l, key=lambda x: x[1])

m = int(input())

for x, y, r in [[int(i) for i in input().split()] for _ in range(m)]:
    print(x, y, r)
