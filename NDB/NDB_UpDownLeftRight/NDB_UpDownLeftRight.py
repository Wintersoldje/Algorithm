n = int(input())
m = list(map(str, input().split()))

x, y = 1, 1
# U D 일때 x값의 변화
dx = [0, 0, -1, 1]
# L R 일때 y값의 변화
dy = [-1, 1, 0, 0]
dir_list = ['L', 'R', 'U', 'D']

for a in m:
    for i in range(len(dir_list)):
        if a == dir_list[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #outofrange 처리
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)