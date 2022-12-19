# 문제

[2665번: 미로만들기](https://www.acmicpc.net/problem/2665)

# 풀이

처음에는 BFS로 탐색을 하면서 벽이 있으면 지워주는 방식을 생각하였지만,,

검은방을 흰방으로 바꾸는 횟수를 최소화 해야 하기 때문에 다익스트라 알고리즘을 사용하였다.

검은방을 방문할 경우 cnt를 +1해주고 힙에 넣어주면 반복문을 돌면서 cnt가 가장 낮은 값이 우선적으로 나오기 때문에 x = n-1, y = n-1일때 cnt값이 정답이 된다.

```python
import sys
import heapq
n = int(input())

table = [list(map(int, input())) for _ in range(n)]
check = [[False] * n for _ in range(n)] #방문 여부 확인

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dijikstra(x, y):
    heap = []
    heapq.heappush(heap, (0, x, y))
    check[x][y] = True #출발지점 방문 처리

    while heap:
        cnt, c_x, c_y = heapq.heappop(heap)

        if c_x == n-1 and c_y == n-1: # 종료지점에 도착했을때의 cnt가 정답
            return cnt

        for i in range(4):
            nx = c_x + dx[i]
            ny = c_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: #범위에 안 들어있으면 무시
                continue

            if check[nx][ny]: #방문 했으면 무시
                continue

            check[nx][ny] = True #방문 처리

            if table[nx][ny] == 0: # 방문한게 벽이면 CNT+1 해주고 heap에 삽입
                table[nx][ny] = 1
                heapq.heappush(heap, (cnt+1, nx, ny))
            else:
                heapq.heappush(heap, (cnt, nx, ny))

print(dijikstra(0,0))
```
