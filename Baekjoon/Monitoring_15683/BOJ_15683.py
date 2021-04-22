from collections import deque
from copy import deepcopy


n, m = map(int, input().split())
area = n * m
list_map = [list(map(int, input().split())) for _ in range(n)]
ans = 0
cctv = []
cctv_5 = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if list_map[i][j] != 0 and list_map[i][j] != 6:
            cctv.append((i, j, list_map[i][j]))
            area -= 1
        if list_map[i][j] == 6:
            area -= 1
        if list_map[i][j] == 5:
            cctv_5.append((i, j))

def count():
    global ans
    for i in range(n):
        for j in range(m):
            if list_map[i][j] == 0:
                ans += 1

def dfs(start):
    global ans, tmp
    if start == len(cctv):
        tmp = deepcopy(list_map)
        c = 0
        for i in range(len(cctv)):
            x, y, dir = cctv[i]
            if dir == 1:
                c += move(x, y, dir_q[i])
            elif dir == 2:
                c += move(x, y, dir_q[i])
                c += move(x, y, (dir_q[i] + 2) % 4)
            elif dir == 3:
                c += move(x, y, dir_q[i])
                c += move(x, y, (dir_q[i] + 1) % 4)
            elif dir == 4:
                c += move(x, y, dir_q[i])
                c += move(x, y, (dir_q[i] + 1) % 4)
                c += move(x, y, (dir_q[i] + 2) % 4)
        ans = min(ans, area - c)
        return


    for i in range(4):
        dir_q.append(i)
        dfs(start + 1)
        dir_q.pop()

def move(x, y, dir):
    cnt = 0
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not 0 <= nx < n or not 0 <= ny < m or tmp[nx][ny] == 6:
            return cnt
        if 0 < tmp[nx][ny] < 6 or tmp[nx][ny] == -1:
            x, y = nx, ny
            continue
        tmp[nx][ny] = -1
        cnt += 1
        x, y = nx, ny

for i in range(len(cctv_5)):
    x, y = cctv_5[i]
    for i in range(4):
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if not 0 <= nx < n or not 0 <= ny < m or list_map[nx][ny] == 6:
                break
            if 0 < list_map[nx][ny] < 6 or list_map[nx][ny] == -1:
                continue
            list_map[nx][ny] = -1
            area -= 1

dir_q = deque()

ans = area
dfs(0)
print(ans)