from itertools import combinations

n, m = map(int, input().split())
list_map = [list(map(int,input().split())) for i in range(n)]

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if list_map[i][j] == 1:
            home.append((i,j))
        elif list_map[i][j] == 2:
            chicken.append((i,j))

pick_chicken = list(combinations(chicken,m))
result = [0] * len(pick_chicken)

for i in home:
    for j in range(len(pick_chicken)):
        a = 100
        for k in pick_chicken[j]:
            tmp = abs(i[0]-k[0]) + abs(i[1]- k[1])
            a = min(a, tmp)
        result[j] += a

print(min(result))