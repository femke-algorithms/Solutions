def main():
    n = int(input())
    l = [] 
    for _ in range(n):
        name, f, s = [i for i in input().split()]
        l.append({
            'name': name,
            'f': float(f),
            's': float(s),
        }) 

    f = sorted(l.copy(), key=lambda x: x['f'])
    s = sorted(l.copy(), key=lambda x: x['s'])

    b = {'time': 10000000.0}

    for runner in f[:4]:
        included = False
        time = [runner['f']]
        runners = [runner['name']]
        for sec in s[:3]:
            if runner['name'] != sec['name']:
                time.append(sec['s'])
                runners.append(sec['name'])
            else: 
                included = True
        if included: 
            time.append(s[3]['s'])
            runners.append(s[3]['name'])
        
        if sum(time) < b['time']:
            b['time'] = sum(time)
            b['runners'] = runners
            

    print(b['time'])
    for r in b['runners']:
        print(r)


if __name__ == '__main__':
    main()




'''
6
ASHMEADE 9.90 8.85
BLAKE 9.69 8.72
BOLT 9.58 8.43
CARTER 9.78 8.93
FRATER 9.88 8.92
POWELL 9.72 8.61




35.54
CARTER
BOLT
POWELL
BLAKE



9
AUSTRIN 15.60 14.92
DRANGE 15.14 14.19
DREGI 15.00 14.99
LAAKSONEN 16.39 14.97
LUNDSTROM 15.83 15.35
MARDELL 13.36 13.20
POLACEK 13.05 12.55
SANNEMO 15.23 14.74
SODERMAN 13.99 12.57


52.670000
MARDELL
POLACEK
SODERMAN
DRANGE
'''
