

def main():
    s = input().split()

    d = {}

    for i in s:
        if i in d:
            print('no')
            return
        d[i] = True

    print('yes')

main()