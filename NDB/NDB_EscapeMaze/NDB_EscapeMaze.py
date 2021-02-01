from collections import deque

n, m = map(int, input().split())

list_maze = []
for i in range(n):
    list_maze.append(list(map(int, input())))

#상하좌우 움직임
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        #상하좌우 움직이면서 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위에 없으면 넘어가기
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽이면 넘어가기
            if list_maze[nx][ny] == 0:
                continue
            # 첫 방문이면 넣어서 움직이기
            if list_maze[nx][ny] == 1:
                list_maze[nx][ny] = list_maze[x][y] + 1
                queue.append((nx,ny))
    # 최종 마지막 출구에서 결과값 리턴
    return list_maze[n-1][m-1]

print(bfs(0,0))