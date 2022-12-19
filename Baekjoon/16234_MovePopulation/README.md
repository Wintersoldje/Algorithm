# 문제

[16234번: 인구 이동](https://www.acmicpc.net/problem/16234)

# 풀이

처음에는 경계가 허물어지는 구간만 구하고 그걸 연결시켜줘야 겠다는 생각을 하였는데 굳이 그럴 필요없이 방문하지 않은 부분이 어디와 연결이 되어있는지를 확인해주고 하나씩 방문하면서 그 부분에 대해서 연결해주는 방식으로 하면 된다.

1. 모든 map의 부분을 0으로 방문 안한 처리를 해준다. (visited 배열 만듦)
2. bfs를 통해 연결된 부분을 찾아준다.
    1. 처음 방문한 x,y 좌표를 큐에 넣어준다.
    2. 그 큐와 인접한 부분의 차가 해당 범위에 포함되고 방문하지 않은 노드라면 방문처리해준다.
    3. 또한 tmp 리스트에 추가해줘서 결과로 리턴한다.
3. 모두 다 방문처리가 되었으면 while문을 나온다.

```python
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
```
https://jewin.notion.site/ba8016dc3f5048b98700a61af6bb1a6b
