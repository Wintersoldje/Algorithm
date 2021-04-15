
def dfs(cnt, result, a, s, m, d):
    global max_result
    global min_result
    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if a:
        dfs(cnt+1, result + list_num[cnt], a-1, s, m, d)
    if s:
        dfs(cnt+1, result - list_num[cnt], a, s-1, m, d)
    if m:
        dfs(cnt+1, result * list_num[cnt], a, s, m-1, d)
    if d:
        dfs(cnt+1, -(-result//list_num[cnt]) if result < 0 else result // list_num[cnt], a, s, m, d-1)

n = int(input())
list_num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_result = -1000000001
min_result = 1000000001
dfs(1, list_num[0], add, sub, mul, div)
print(max_result)
print(min_result)