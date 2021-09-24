# 문제

[17144번: 미세먼지 안녕!](https://www.acmicpc.net/problem/17144)

# 풀이

문제의 요구사항 순서대로 해 보니 바로 풀렸다.

우선 spread 함수를 만들어서 매초 미세먼지가 퍼저 나갈 수 있게 만들었다. 여기서는 다른 칸도 동시에 퍼저야 했기 때문에 퍼지고 그 자리에 남은 먼지를 저장해두고 퍼진 먼지는 따로 리스트(tmp_list)를 만들어서 둘을 더해 주었다.

공기 청정기의 공기 방향은 공기 청정기에서는 0이 나오고 나머지 한 칸씩 밀려 나게 했다. 여기서는 tmp를 두어 직전 먼지 량을 저장해두고 먼지가 벽에 닿으면 위에는 반시계 방향 아래는 시계 방향으로 돌게 하기 위해서 dir를 -1, +1 해주면서 돌았다. 또한 범위 설정을 공기청정기의 위치로 범위를 지정해 주어서 공기청정기를 기준으로 넘어가지 않게 해주었다.

```python
r, c, t = map(int, input().split())
list_map = [list(map(int, input().split())) for i in range(r)]
clean = []
for i in range(r):
    for j in range(c):
        if list_map[i][j] == -1:
            clean.append([i,j])
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def spread(l):
    tmp_map = [[0] * c for _ in range(r)] # 뿌려진 먼지를 저장하는 리스트
    for i in range(r):
        for j in range(c):
            if l[i][j] == -1: #공기청정기가 위치해 이쓰면 스킵
                continue
            if l[i][j] != 0:
                cnt = 0
                for k in range(4): # 먼지 주변 뿌려질 먼지를 계산
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if not(0 <= nx < r and 0 <= ny < c) or l[nx][ny] == -1:
                        continue
                    else:
                        tmp_map[nx][ny] += l[i][j] // 5
                        cnt += 1
                l[i][j] -= (l[i][j] // 5) * cnt
    for i in range(r): # 뿌려진 먼지와 남은 먼지를 합쳐줌
        for j in range(c):
            l[i][j] += tmp_map[i][j]
    return l

def cleaner():
    first = clean[0] #공기청정기의 윗부분
    second = clean[1] #공기청정기의 아랫부분
    fix_x, fix_y = first[0], first[1]
    fix2_x, fix2_y = second[0], second[1]

    x, y = first[0], first[1]
    x2, y2 = second[0], second[1]

    dir = 0
    tmp = 0
    while True: # 공기 청정기 윗 부분 돌면서 한 칸씩 밀어주는 부분
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not(0 <= nx <= fix_x and 0 <= ny < c):
            dir = (dir - 1) % 4
            continue

        if list_map[nx][ny] == -1:
            break
        tt = list_map[nx][ny]
        list_map[nx][ny] = tmp
        tmp = tt
        x = nx
        y = ny
    tmp = 0
    dir = 0

    while True:# 공기 청정기 아랫 부분 돌면서 한 칸씩 밀어주는 부분
        nx = x2 + dx[dir]
        ny = y2 + dy[dir]
        if not(fix2_x <= nx < r and 0 <= ny < c):
            dir = (dir + 1) % 4
            continue
        if list_map[nx][ny] == -1:
            break
        tt = list_map[nx][ny]
        list_map[nx][ny] = tmp
        tmp = tt
        x2 = nx
        y2 = ny

for i in range(t):
    list_map = spread(list_map)
    cleaner()

result = 0
for i in list_map:
    result += sum(i)
result += 2

print(result)
```
https://jewin.notion.site/89e4407e96074872b77d839637d0bfc4
