n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0  or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        #상하좌우 확인
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)