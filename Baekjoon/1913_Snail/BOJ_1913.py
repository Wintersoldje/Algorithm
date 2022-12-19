n = int(input())
m = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir = 0
num = n**2
array = [[0]*n for _ in range(n)]

array[0][0] = num
cx = 0
cy = 0
rst_x = 0
rst_y = 0

while(array[n//2][n//2] != 1):
    nx = cx + dx[dir % 4]
    ny = cy + dy[dir % 4]
    if not(0 <= nx < n and 0 <= ny < n) or array[nx][ny] != 0:
        dir += 1
        continue
    if num == m:
        rst_x = cx + 1
        rst_y = cy + 1
    num -= 1
    array[nx][ny] = num
    cx = nx
    cy = ny

for arr in array:
    for i in range(n):
        print(arr[i], end=' ')
    print()

print(rst_x, rst_y)
