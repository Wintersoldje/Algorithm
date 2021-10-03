# 문제

[19236번: 청소년 상어](https://www.acmicpc.net/problem/19236)

# 풀이

1. list_map에는 map그대로를 저장하되 해당 위치에 [물고기번호, 방향]을 묶어서 넣어줬다
2. fish에는 물고기 번호에 해당하는 인덱스에 그 물고기의 위치를 넣어줬다.
3. 물고기를 이동시키는 함수를 만들었다.(move_fish)
    1. 물고기 1번(편의를 위해 -1번, 즉, 0번부터)부터 돌면서 이동
    2. 이동 조건을 충족하면 해당 위치 바꿔주고 list_map,fish를 다 바꿔준다.
4. 찾을때는 dfs를 이용한다.
    1. 상어의 위치에서 방향으로 계속 가면서 dfs로 탐색한다.
    2. 탐색에 들어갈때는 해당 위치에 상어가 물고기를 먹고 상어가 물고기를 먹은 최종 map을 넘겨주기 위해서 기존의 map을 저장해둔다.
    3. dfs에서 나오면 원래 map의 상태로 되돌려 놓는다.

```python
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
```

https://jewin.notion.site/97cdda1f63384ec786c9ede7b1dd2a08
