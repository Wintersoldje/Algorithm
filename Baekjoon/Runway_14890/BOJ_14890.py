n, l = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

def solution(x, y, dx, dy):
    k = 1
    for _ in range(n-1):
        nx = x + dx
        ny = y + dy
        diff = maps[nx][ny] - maps[x][y]
        if abs(diff) > 1:
            return 0
        if diff == 1:
            if k >= l:
                k = 0
            else:
                return 0
        if diff == -1:
            if k >= 0:
                k = -l
            else:
                return 0
        k += 1
        x, y = nx, ny
    if k >= 0:
        return 1
    else:
        return 0

result = 0
for i in range(n):
    result += solution(0, i, 1, 0)
    result += solution(i, 0, 0, 1)

print(result)
