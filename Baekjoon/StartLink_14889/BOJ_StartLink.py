from itertools import combinations
n = int(input())
list_table = [list(map(int, input().split())) for _ in range(n)]
members = [i for i in range(n)]
poss_team = []

#모든 조합을 구함
for team in list(combinations(members, n//2)):
    poss_team.append(team)

min_val = 100000
#조합을 보면서 조합의 반대 부분이 -i-1번째라는 사실만 알면 쉽게 풀 수 있다.
for i in range(len(poss_team)//2):
    team = poss_team[i]
    start_A = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            start_A += list_table[member][k]
    team2 = poss_team[-i-1]
    start_B = 0
    for j in range(n//2):
        member = team2[j]
        for k in team2:
            start_B += list_table[member][k]
    min_val = min(min_val, abs(start_B - start_A))
print(min_val)