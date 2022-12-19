dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
data = [list(map(int, input().split())) for _ in  range(n)]
dir = [[]for _ in range(n)]

#x, y 시작 지점 d처음 방향 g 세대
#방향과 세대에 따라서 방향 정해줌
for i in range(n):
    x, y, d, g = data[i]
    dir[i].append(d)
    for _ in range(g):
        reverse = list(reversed(dir[i]))
        for j in reverse:
            dir[i].append((j + 1) % 4)

arr = [[False] * 101 for _ in range(101)]

for i in range(n):
    x, y, d, h = data[i]
    arr[y][x] = True
    for j in dir[i]:
        x, y = x + dx[j], y + dy[j]
        if 0 <= x <= 100 and 0 <= y <= 100:
            arr[y][x] = True

answer = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
            answer += 1

print(answer)
