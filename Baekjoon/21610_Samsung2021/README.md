# 문제

[21610번: 마법사 상어와 비바라기](https://www.acmicpc.net/problem/21610)

# 풀이

우선 order만큼 반목문을 돌면서 수행한다.

1. 구름을 옮겨준다. 
    1. 처음에는 가는 숫자만큼 for 문을 돌았는데 그렇게 하면 시간초과가 나서 방법을 바꿨다.
    2. 곱하기 num 해주고 n 을 나눈 나머지로 연산해주면 된다.
    3. 그리고 최종 구름 위치를 visited 리스트를 만들어 방문 표시 해준다.
2. 대각선 위치에 있으면 +1 을 해준다.
    1. 조건에 맞지 않으면 pass 한다
3. 구름 리스트를 비워준다.
4. 구름이 생기는 위치를 보고 만든다.
    1. 방문 했던 위치면 넘어간다.
5. 반복 후 모든 숫자를 더해준다.

```python
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
list_map = [list(map(int, input().split())) for _ in range(n)]
list_order = [list(map(int, input().split())) for _ in range(m)]
list_clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

for dir, num in list_order:
    # 구름 옮기기
    tmp_cloud = []
    visited = [[False] * n for _ in range(n)]

    for cloud in list_clouds:
        x, y = cloud[0], cloud[1]
        nx = (x + dx[dir] * num) % n
        ny = (y + dy[dir] * num) % n
        list_map[nx][ny] += 1 # 땅에 +1
        visited[nx][ny] = True
        tmp_cloud.append([nx, ny])
    list_clouds = tmp_cloud

    # 대각선 증가
    for cloud in list_clouds:
        x, y = cloud[0], cloud[1]
        if 0<=x-1<n and 0<=y+1<n:#우측상단
            if list_map[x-1][y+1] > 0:
                list_map[x][y] += 1
        if 0 <= x-1 < n and 0 <= y-1 < n:#좌측상단
            if list_map[x-1][y-1] > 0:
                list_map[x][y] += 1
        if 0 <= x+1 < n and 0 <= y-1 < n:#좌측하단
            if list_map[x+1][y-1] > 0:
                list_map[x][y] += 1
        if 0 <= x+1 < n and 0 <= y+1 < n:#좌측하단
            if list_map[x+1][y+1] > 0:
                list_map[x][y] += 1

    list_clouds = []
    # 구름 생김
    for i in range(n):
        for j in range(n):
            if list_map[i][j] >= 2 and visited[i][j] == False:
                list_map[i][j] -= 2
                list_clouds.append([i,j])

answer = 0
for i in list_map:
    answer += sum(i)

print(answer)
```

https://jewin.notion.site/d9663b2887df48438ac8742aa1105419
