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


