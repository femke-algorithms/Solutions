# pylint: disable-all

def main():
    n, m = [int(i) for i in raw_input().split()]

    d = {}

    for day in range(m):
        d[raw_input()] = 1
        if len(d.items()) == n:
            print(day + 1)
            return 

    print('paradox avoided')

if __name__ == '__main__':
    main()
