# 문제

[17142번: 연구소 3](https://www.acmicpc.net/problem/17142)

# 풀이

문제에 나와있는대로 접근하였고, 바이러스가 있는 위치를 따로 저장해두고, 조합을 이용해 어떤 바이러스를 활성화 시킬지 정해줍니다. 이는 BFS를 이용해 하나씩 비교해보고 결과적으로 각각의 경우에서 경로의 최소 시간을 구해줍니다.

1. 바이러스가 있는 위치를 조합해서 모든 경우의 수를 구함
2. check함수를 이용해 바이러스가 퍼진 시간을 구함 
    1. 다 안퍼졌으면 -1 리턴
    2. 퍼질게 없으면 0
    3. 다 잘 퍼졌으면 가장 큰 수인 시간 리턴
3. 모든 바이러스의 조합에 해당하는 부분을 bfs로 계산해 가장 작은 시간을 구함

```python
from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
list_map = [list(map(int, input().split())) for _ in range(n)]
list_virus = []
for i in range(n):
    for j in range(n):
        if list_map[i][j] == 2: # 바이러스는 list_virus에 좌표를 넣어주고, 카운트의 편의를 위해 2를 -2로 1은 -1로 전환
            list_map[i][j] = -2
            list_virus.append([i,j,1])
        if list_map[i][j] == 1:
            list_map[i][j] = -1

com_virus = list(combinations(list_virus, m)) # 조합을 통해 모든 경우의 수 구함

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = int(1e9)

def check(board): # 보드를 확인하며 0이 있으면 즉, 바이러스가 퍼지지 않으면 -1리턴
    num = -1000001
    for i in range(n):
        for j in range(n):
            num = max(num, board[i][j])
            if board[i][j] == 0:
                return -1
    if num == -1 or num == -2:
        num = 0
    return num

for tmp in com_virus: #모든 조합의 바이러스 체크(bfs)
    new_map = copy.deepcopy(list_map)
    q = deque()

    for i in range(m):
        q.append(tmp[i])
        new_map[tmp[i][0]][tmp[i][1]] = -1 #바이러스 시작 부분은 벽인 -1로 바꿔줌
    # print("new", new_map)
    while q:
        # print("new", new_map)
        x, y, nn = q.popleft()
        for j in range(4): # 바이러스의 위 아래 좌 우 퍼트릴 수 있는지 확인
            nx = x + dx[j]
            ny = y + dy[j]
            # print(nx,ny)
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if new_map[nx][ny] == -1: #벽이면 통과
                continue
            if new_map[nx][ny] == -2: #비활성화 바이러스이면 해당 바이러스도 벽 처리 해주고 해당 바이러스도 q에 넣어줌
                new_map[nx][ny] = -1
                q.append([nx, ny, nn+1])
                continue
            if new_map[nx][ny] != 0: #이미 누가 지나간거라서 패스
                continue
            else: #0일 경우인데 여기서는 해당 보드에 time인 nn을 넣어주고 그 좌표를 queue에 넣어줌
                new_map[nx][ny] = nn 
                q.append([nx, ny, nn+1])

    # print(new_map)

    tmp = check(new_map) # check를 통해 확인
    if tmp == -1:
        continue
    ans = min(ans, tmp) # 최소 시간 구하기

if ans == int(1e9): # 최소로 안들어갔으면 실패이므로 -1
    ans = -1
print(ans)
```

[https://jewin.notion.site/3-1aac338b269743cb99fa4b305d770fb2](https://www.notion.so/3-1aac338b269743cb99fa4b305d770fb2)
