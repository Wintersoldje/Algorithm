n, m, k = map(int, input().split())
list_map = [list(map(int ,input().split())) for _ in range(n)] # map
list_dir = list(map(int, input().split())) # 각 상어의 방향
list_pri = [[] for _ in range(m)]
for i in range(m):
    list_pri[i] = [list(map(int, input().split())) for _ in range(4)]

smell = [[[0,0]] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def smell_map():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if list_map[i][j] != 0:
                smell[i][j] = [list_map[i][j], k]

def move():
    new_data = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if list_map[x][y] != 0:
                dir = list_dir[list_map[x][y] - 1]-1
                flag = False

                for d in list_pri[list_map[x][y]-1][dir]:
                    nx = x + dx[d-1]
                    ny = y + dy[d-1]
                    if not(0 <= nx < n and 0 <= ny < n):
                        continue
                    if smell[nx][ny][1] == 0:
                        list_dir[list_map[x][y] - 1] = d
                        if new_data[nx][ny] == 0:
                            new_data[nx][ny] = list_map[x][y]
                        else:
                            new_data[nx][ny] = min(list_map[x][y], new_data[nx][ny])
                        flag = True
                        break

                if flag == True:
                    continue

                for d in list_pri[list_map[x][y]-1][dir]:
                    nx = x + dx[d-1]
                    ny = y + dy[d-1]
                    if not(0 <= nx < n and 0 <= ny < n):
                        continue
                    if smell[nx][ny][0] == list_map[x][y]:
                        list_dir[list_map[x][y]-1] = d
                        new_data[nx][ny] = list_map[x][y]
                        break
    return new_data

answer = 0
while True:
    smell_map()
    new_map = move()
    tmp = 0
    for i in range(n):
        tmp += sum(new_map[i])
    answer += 1
    if tmp == 1:
        break
    if answer >= 1000:
        answer = -1
        break
    list_map = new_map
print(answer)