n, m = [int(i) for i in input().split()]

if n == m:
    if not n:
        print('Not a moose')
    else:
        print('Even ' + str(n * 2))

else:
    print('Odd ' + str(max(n, m) * 2))
