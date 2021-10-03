from copy import deepcopy

list_map = [[] for _ in range(4)]
fish = [[] for _ in range(16)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
ans = 0
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        list_map[i].append([tmp[j]-1, tmp[j+1]-1])
        fish[tmp[j]-1] = [i, j//2]
def move_fish(sx, sy):
    for i in range(16):
        if fish[i]:
            x, y = fish[i][0], fish[i][1]
            for _ in range(9):
                nx, ny = x + dx[list_map[x][y][1]], y + dy[list_map[x][y][1]]
                if not(0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                    list_map[x][y][1] = (list_map[x][y][1] + 1) % 8
                    continue
                if list_map[nx][ny]:
                    fish[list_map[nx][ny][0]] = [x,y]
                list_map[nx][ny] , list_map[x][y] = list_map[x][y], list_map[nx][ny]
                fish[i] = [nx, ny]
                break

def dfs(x, y, d, cnt):
    global ans, list_map, fish
    move_fish(x,y)
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if not(0<= nx < 4 and 0 <= ny < 4):
            ans = max(ans, cnt)
            break
        if not list_map[nx][ny]:
            x, y = nx, ny
            continue
        tmp_fish, tmp_map = deepcopy(fish), deepcopy(list_map)
        tmp_a, tmp_b = fish[list_map[nx][ny][0]], list_map[nx][ny]
        fish[list_map[nx][ny][0]], list_map[nx][ny] = [], []
        dfs(nx, ny, tmp_b[1], cnt + tmp_b[0] + 1)
        fish, list_map = tmp_fish, tmp_map
        fish[list_map[nx][ny][0]], list_map[nx][ny] = tmp_a, tmp_b
        x, y = nx, ny

d, cnt = list_map[0][0][1], list_map[0][0][0] + 1
fish[list_map[0][0][0]], list_map[0][0] = [], []
dfs(0, 0, d, cnt)
print(ans)

