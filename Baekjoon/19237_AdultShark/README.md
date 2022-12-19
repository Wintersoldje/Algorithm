# 문제

[19237번: 어른 상어](https://www.acmicpc.net/problem/19237)

# 풀이

문제를 이해하는데 시간이 조금 오래 걸렸다. map을 돌면서 smell 맵을 하나 따로 만들어서 향기가 남아있는지 확인을 해줬고, 처음에는 k만큼의 향을 저장해 둔 뒤 한 번 돌고 나면 -1 씩 해주면서 향을 지웠다.

1. smell_map 함수를 이용해서 처음 map의 위치에 있는 상어들의 향을 뿌려준다. 향은 [상어 번호, 남은 향] 이런식으로 list를 만들어준다.
2. 그리고 상어를 이동시킨다. 이동 시킬때는 방향을 저장해 둔 우선순위 대로 정한다. 
3. 정한 방향은 다음 움직임에 쓰여야 하므로 list_dir에 저장해둔다.
4. 만약 4방이 향으로 가득 찼다면 자신의 위치로 간다.(여기서 new_data라는 맵을 썼는데, 이동된 상어를 따로 리스트를 만들어서 이동시키고, 함수의 리턴값으로 그 리스트를 반환해주어 갱신시켜준다.)
5. 1000번 돌면서 map 의 총 합이 1이면 종료해준다.

```python
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
```

https://jewin.notion.site/313ec04892f7417b9d25ed9bc31f2db1
