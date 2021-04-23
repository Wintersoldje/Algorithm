from collections import deque

def spread():
    for i in range(r):
        for j in range(c):
            if list_map[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if not (0 <= nx < r and 0 <= ny < c):
                        continue
                    if list_map[i][j] < 5:
                        continue
                    if (nx, ny) == (cleaner_loc[0], 0):
                        continue
                    if (nx, ny) == (cleaner_loc[1], 0):
                        continue
                    list_map2[nx][ny] = list_map2[nx][ny] + list_map[i][j]//5
                    cnt += 1
                list_map2[i][j] = list_map2[i][j] + list_map[i][j] - list_map[i][j]//5*cnt


def cleaner_run():
    #위
    x, y = cleaner_loc[0]
    for i in range(x-2, -1, -1):
        list_map2[i+1][0] = list_map2[i][0]
    for i in range(1, c):
        list_map2[0][i-1] = list_map2[0][i]
    for i in range(1, x+1):
        list_map2[i-1][-1] = list_map2[i][-1]
    for i in range(c-2, 0, -1):
        list_map2[x][i+1] = list_map2[x][i]
    #아래
    list_map2[x][1] = 0
    x, y = cleaner_loc[1]
    for i in range(x+2,r):
        list_map2[i-1][0] = list_map2[i][0]
    for i in range(1, c):
        list_map2[-1][i-1] = list_map2[-1][i]
    for i in range(r-2, x-1, -1):
        list_map2[i+1][-1] = list_map2[i][-1]
    for i in range(c-2, 0, -1):
        list_map2[x][i+1] = list_map2[x][i]
    list_map2[x][1] = 0


r, c, t = map(int, input().split())
list_map = [list(map(int, input().split())) for _ in range(r)]
list_map2 = [[0]*c for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cleaner_loc = []
for i in range(r):
    if list_map[i][0] == -1:
        cleaner_loc.append((i,0))

spread()
cleaner_run()

for i in range(t-1):
    list_map = list_map2.copy()
    list_map2 = [[0]*c for _ in range(r)]
    spread()
    cleaner_run()

sum = 0
for i in range(r):
    for j in range(c):
        if list_map2[i][j] > 0 :
            sum = sum + list_map2[i][j]

print(sum)