import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(tmp):
    if tmp == parent[tmp]:
        return tmp
    return(find(parent[tmp]))

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b

for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a,b)


