from collections import deque

n, l, r = map(int, input().split())
list_map = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x, y):
    q = deque()
    q.append([x,y])
    tmp = []
    tmp.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(list_map[nx][ny] - list_map[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    tmp.append([nx,ny])
    return tmp

cnt = 0
while True:
    visited = [[0] * n for _ in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                temp = bfs(i,j)
                if len(temp) > 1:
                    isTrue = True
                    num = sum([list_map[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        list_map[x][y] = num
    if not isTrue:
        break
    cnt += 1

print(cnt)
