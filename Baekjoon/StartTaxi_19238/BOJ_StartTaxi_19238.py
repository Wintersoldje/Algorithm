from collections import deque

n, m , f = map(int, input().split())
list_map = [list(map(int, input().split())) for _ in range(n)]
c_x, c_y = map(int, input().split()) #현재 위치
c_x, c_y = c_x-1, c_y-1

list_guest = []
list_goal = []

for _ in range(m):
    a, b, c, d = map(int, input().split())
    list_guest.append([a-1,b-1])
    list_goal.append([a-1, b-1, c-1, d-1])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, ff):
    global c_x, c_y
    global list_guest
    q = deque()
    q.append([x, y, 0])
    visited = [[False] * n for _ in range(n)]
    guest = []
    if [x,y] in list_guest:
        guest.append([x, y, 0])

    while q:
        cx, cy, num = q.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if not (0 <= nx < n and 0 <= ny < n) or list_map[nx][ny] == 1 or visited[nx][ny] == True:
                continue
            if [nx, ny] in list_guest:
                if len(guest) > 0:
                    if guest[0][2] < num+1:
                        break
                guest.append([nx, ny, num+1])
            q.append([nx, ny, num+1])
            visited[nx][ny] = True
    guest = sorted(guest, key=lambda x:(x[2], x[0], x[1]))
    xx, yy = 0, 0
    if len(guest) == 0:
        return [0,0,-1]
    for aa, bb, cc, dd in list_goal:
        if guest[0][0] == aa and guest[0][1] == bb:
            if ff - guest[0][2] < 0:
                return [0,0,-1]
            else:
                c_x, c_y = aa, bb #출발지 현재 위치로 두기
                xx, yy = cc, dd  #목적지
                break

    list_guest.remove([guest[0][0], guest[0][1]])
    ff -= guest[0][2]
    tmp_ff = find_goal_bfd(xx, yy, ff)

    if tmp_ff == -1:
        return [xx, yy, -1]
    return [xx, yy, tmp_ff]

def find_goal_bfd(f_x, f_y, f):
    # print("f", f)
    q = deque()
    q.append([c_x, c_y, 0])
    visited = [[False] * n for _ in range(n)]
    while q:
        cx, cy, num = q.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if not (0 <= nx < n and 0 <= ny < n) or list_map[nx][ny] == 1 or visited[nx][ny] == True:
                continue

            if nx == f_x and ny == f_y:
                if f - (num+1) < 0:
                    return -1
                else:
                    return f - (num + 1) + ((num+1) * 2)
            q.append([nx, ny, num + 1])
            visited[nx][ny] = True
    return -1

for i in range(m):
    aaa, bbb, ccc = bfs(c_x, c_y, f)
    if ccc != -1:
        c_x, c_y = aaa, bbb
        f = ccc
    else:
        f = -1
        break

print(f)
