n, m = map(int,input().split())
sx, sy, direct = map(int, input().split())

#움직임을 확인하는 배열
d = [[0]*m for _ in range(n)]
#현위치 지정
d[sx][sy] = 1
#맴 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 왼쪽으로 방향을 바꾸는 함수
def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3


count = 1
turn_time = 0
while True:
    turn_left()
    # 방향 앞에 갈 수 있는지 판단
    nx = sx + dx[direct]
    ny = sy + dy[direct]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 다 보고 없으면 후진
    if turn_time == 4:
        nx = x - dx[direct]
        ny = y - dy[direct]

        if array[nx][ny] == 0:
            x = nx
            y = ny
            count += 1
        else:
            break
        turn_time = 0

print(count)
