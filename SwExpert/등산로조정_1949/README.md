# 문제

[SW Expert Academy](https://swexpertacademy.com/main/code/problem/problemDetail.do)

# 풀이

처음에는 BFS로 접근하였다가 처리해야할 조건들이 너무 많아서 DFS로 전환하였다. 

이런 문제 처럼 무엇을 놓고 다시 돌려 놓고 하는 문제는 DFS로 접근해야겠다...

1. map에서 가장 큰 수를 찾아서 좌표를 list_top에 저장해둔다.
2. List_top을 돌면서 dfs를 수행한다.
    1. 종료조건은 따로 걸지 않고, 각각의 cnt 값중 큰 값을 넣어줬다. 
    2. visited 처리를 해주고, 
    3. 4방향을 돌면서 다음 갈 방향이 방문하지 않은 칸이면 비교해준다.
        1. 다음 칸이 자기 보다 작으면 dfs로 재귀
        2. -k 한 값이 나보다 작으면 
            1. k가 유효하면 현재보다 -1 인 값을 넣어준다. (왜냐하면 최대 K만큼 팔 수 있으니까 다다음칸에 영향을 안 주기 위해)
        3. dfs에서 나오면 원래 값으로 돌려준다.
    4. 방문 안한 처리를 해준다.
3. 최종적으로 result 에는 가장 큰 값이 남게 된다. (cnt+1을 해주는 이유는 자신이 마지막 칸일 경우 자신의 초가 카운트 되지 않기 때문)

```python
from collections import deque
import copy

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(x, y, kk, cnt):
    global result
    if result < cnt+1:
        result = cnt+1
    visited[x][y] = 1
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if visited[nx][ny] == 0:
            if list_map[nx][ny] < list_map[x][y]:
                dfs(nx, ny, kk, cnt+1)
            elif list_map[nx][ny] - k < list_map[x][y]:
                if kk > 0:
                    tmp = list_map[nx][ny]
                    list_map[nx][ny] = list_map[x][y] - 1
                    dfs(nx, ny, kk-1, cnt+1)
                    list_map[nx][ny] = tmp
    visited[x][y] = 0

for test_case in range(1, T + 1):
    count_list = []
    result = -1
    n, k = map(int, input().split())
    list_map = [list(map(int, input().split())) for _ in range(n)]
    list_top = []
    mmax = -10001
    cnt = 1
    q = deque()
    for i in range(n):
        mmax = max(mmax, max(list_map[i]))

    for i in range(n):
        for j in range(n):
            if list_map[i][j] == mmax:
                list_top.append([i,j])

    visited = [[0] * n for _ in range(n)]

    for a,b in list_top:
        dfs(a,b,1,0)
    print(f"#{test_case} {result}")
```

https://jewin.notion.site/SWexpert-9c565ddc1f434fdcaf20b28396023783
