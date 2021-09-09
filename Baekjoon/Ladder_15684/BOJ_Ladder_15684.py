n, m, h = map(int, input().split())
list_leg = [list(map(int, input().split())) for i in range(m)]

list_map = [[False] * n for i in range(h)]

for a, b in list_leg:
    list_map[a-1][b-1] = True

def check():
    for start in range(n):
        k = start
        for i in range(h):
            if list_map[i][k]:
                k += 1
            elif k > 0 and list_map[i][k-1]:
                k -= 1
        if start != k:
            return False
    return True

def bf(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    for i in range(x,h):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, n-1):
            if not list_map[i][j] and not list_map[i][j+1]:
                list_map[i][j] = True
                bf(cnt+1, i, j+2)
                list_map[i][j] = False

ans = 4
bf(0,0,0)
print(ans if ans < 4 else -1)