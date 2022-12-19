# 문제

[16236번: 아기 상어](https://www.acmicpc.net/problem/16236)

# 풀이

1. map을 돌면서 상어의 위치 저장, 상어가 있던 위치 0으로 바꿔줌
2. 상어의 크기, 시간, 먹은 갯수를 shark_size, time, feed로 표현
3. BFS로 탐색
    1. 범위 벗어나면 continue
    2. 방문했거나, 아기상어의 크기보다 크다면 continue
    3. 아기 상어가 더 크면, fish리스트에 넣어준다. (좌표, 시간)
4. fish 안에 있는 물고기중에 가장 가까운 물고기를 먹는다. 
5. 3~4번 반복
6. 가장 많이 먹을 수 있을때까지

```python
from collections import deque

n = int(input())
list_map = [list(map(int, input().split())) for _ in range(n)]

cx, cy = 0, 0 # 상어의 위치
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
            cx, cy = i, j #아기상어의 위치를 저장
            list_map[i][j] = 0 #아기상어가 있는 자리 0으로 변환
            flag = True #시간을 아끼기 위한 flag로 반복문 탈출
            break
    if flag == True:
        break

while True: # bfs로 탐색
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
```

https://jewin.notion.site/49a041df1e2c4dd2a4d1eff4b982fa27
