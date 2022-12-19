import copy

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
input_list = [list(map(int, input().split())) for _ in range(n)]
list_map = [[0] * 101 for i in range(101)]
tmp_dir = []
tmp2_dir = []
list_dir = []
for j in range(n):
    x, y, d, g = input_list[j]
    list_map[y][x] = 1 # 방문 하면 1로 바꿔줌
    tmp_dir.append(d) # 원래의 방향을 넣어준다.
    tmp2_dir = []
    for i in range(1,g+1): # tmp_dir에 있는 방향을 다 뽑아서 +1 해준 후 리버스 해서 다시 넣어주면 이동한 방향이 된다.
        for k in range(len(tmp_dir)):
            tmp2_dir.append((tmp_dir[k]+1)%4)
        tmp2_dir.reverse()
        for p in range(len(tmp2_dir)):
            tmp_dir.append(tmp2_dir[p])
        tmp2_dir.clear()
    a = copy.deepcopy(tmp_dir)
    for tmp in tmp_dir: # 해당 방향 대로 이동해준다.
        nx = x + dx[tmp]
        ny = y + dy[tmp]
        list_map[ny][nx] = 1
        x = nx
        y = ny
    list_dir.append(a)
    tmp_dir.clear()
answer = 0

for i in range(100):
    for j in range(100): # 4개의 점이 사각형을 만들면 +1
        if list_map[i][j] == 1 and list_map[i+1][j] == 1 and list_map[i][j+1] == 1 and list_map[i+1][j+1] == 1:
            answer += 1

print(answer)

