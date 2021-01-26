def turn_direct(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    data = [[0] * (n + 1) for _ in range(n)]
    # map info
    for i in range(k):
        a, b = map(int, input().split())
        data[a][b] = 1  # apple

    l = int(input())
    list_turn = []
    for i in range(l):
        a, b = map(str, input().split())
        list_turn.append((int(a), b))
    # 동 남 서 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    q = [(x,y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 < nx and nx < n and 1 < ny and ny < n and data[nx][ny] != 2:
            if data[nx][ny] == 1:
               data[nx][ny] =2
               q.append((nx, ny))
            elif data[nx][ny] == 0:
                data[nx][ny] = 2
                qx, qy = q.pop(0)
                q.append((nx, ny))
                data[qx][qy] = 0




