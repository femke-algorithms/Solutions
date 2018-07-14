def main():
    n, m = [int(i) for i in input().split()]
    teams = {}
    ahead = {}
    for i in range(n):
        teams[i + 1] = [0, 0]

    for _ in range(m):
        t, p = [int(i) for i in input().split()]
        teams[t][0] += 1
        teams[t][1] += p
        
        if t == 1: 
            to_pop = []
            for team, score in ahead.items():
                if not (score[0] > teams[1][0] or (score[0] == teams[1][0] and score[1] < teams[1][1])):
                    to_pop.append(team)
            for i in to_pop:
                ahead.pop(i, None)
        else: 
            if teams[t][0] > teams[1][0] or (teams[t][0] == teams[1][0] and teams[t][1] < teams[1][1]):
                ahead[t] = teams[t]
        
        print(1 + len(ahead))

        



if __name__ == '__main__':
    main()


'''
3 4
2 7
3 5
1 6
1 9

'''
