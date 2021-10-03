from collections import deque

n = int(input())

list_map = [list(map(int, input().split())) for _ in range(n)]

cx, cy = 0, 0
shark_size = 2
time = 0
feed = 0
result = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
flag = False
for i in range(n):
    for j in range(n):
        if list_map[i][j] == 9:
            cx, cy = i, j
            list_map[i][j] = 0
            flag = True
            break
    if flag == True:
        break

# target_shark = []
# for i in range(n):
#     for j in range(n):
#         if list_map[i][j] < shark_size and list_map[i][j] != 0:
#             target_shark.append([i,j])


while True:
    q = deque()
    q.append((cx, cy, 0))
    visited = [[False] * n for _ in range(n)]
    flag = int(1e9)
    fish = []
    while q:
        x, y, count = q.popleft()
        # print(x, y)
        if count > flag:
            break
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if list_map[nx][ny] > shark_size or visited[nx][ny]:
                continue
            if list_map[nx][ny] != 0 and list_map[nx][ny] < shark_size:
                fish.append((nx,ny,count+1))
                flag = count
            visited[nx][ny] = True
            q.append((nx, ny, count+1))
    # print(fish)
    if len(fish) > 0:
        fish.sort()
        x, y, count = fish[0][0], fish[0][1], fish[0][2]
        result += count
        feed += 1
        list_map[x][y] = 0
        if feed == shark_size:
            shark_size += 1
            feed = 0
        cx, cy = x, y
    else:
        break

print(result)
