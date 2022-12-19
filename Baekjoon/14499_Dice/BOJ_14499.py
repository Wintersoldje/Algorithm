n, m, x, y, k = map(int,input().split())
list_map = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0 for _ in range(6)]

#동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while True:
    if len(order) == 0:
        break
    direction = order.pop(0) - 1

    nx = x + dx[direction]
    ny = y + dy[direction]

    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    if direction == 0:
        dice[0], dice[3], dice[5], dice[2] = dice[3] , dice[5], dice[2], dice[0]
    elif direction == 1:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif direction == 2:
        dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]
    elif direction == 3:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]

    if list_map[nx][ny] == 0:
        list_map[nx][ny] = dice[5]
    else:
        dice[5] = list_map[nx][ny]
        list_map[nx][ny] = 0

    x, y= nx, ny
    print(dice[0])

