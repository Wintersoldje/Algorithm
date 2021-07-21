n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
list = [list(map(int, input().split())) for _ in range(m)]
result = 0

list.sort(key=lambda x:x[2])
# print(list)

def find(target):
    if target == parent[target]:
        return target
    return find(parent[target])

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]

for i in range(m):
    a, b, c = list[i]
    if find(a) != find(b):
        union(a,b)
        result += c

print(result)
