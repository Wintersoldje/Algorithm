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









