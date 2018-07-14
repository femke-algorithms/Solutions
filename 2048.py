'''
2 0 0 2
4 16 8 2
2 64 32 4
1024 1024 64 0
0
'''
# 0 - left 1 - up 2 - right 3 - down

board = []

for _ in range(4):
    board.append([int(i) for i in input().split()])

n = int(input())

