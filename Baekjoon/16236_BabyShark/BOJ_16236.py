from collections import deque
INF = 1e9

n = int(input())
list_map = [list(map(int, input().split()))for _ in range(n)]

shark_size = 2

cur_x, cur_y = 0,0

for i in range(n):
    for j in range(n):
        if list_map[i][j] == 9:
            cur_x, cur_y = i, j
            list_map[i][j] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#최단거리 구하기
def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque([(cur_x, cur_y)])
    dist[cur_x][cur_y]= 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if dist[nx][ny] == -1 and list_map[nx][ny] <= shark_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

#먹을 물고기 찾기
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= list_map[i][j] and list_map[i][j] < shark_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0

while True:
    value = find(bfs())

    if value == None:
        print(result)
        break
    else:
        cur_x, cur_y = value[0], value[1]
        result += value[2]

        list_map[cur_x][cur_y] = 0
        ate += 1

        if ate >= shark_size:
            shark_size += 1
            ate = 0