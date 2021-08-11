def find(target):
    global parent
    if target == parent[target]:
        return target
    return find(parent[target])

def union(a, b):
    global parent
    ap = find(a)
    bp = find(b)
    if ap > bp :
        parent[ap] = parent[bp]
    else:
        parent[bp] = parent[ap]

def solution(n, costs):
    global parent
    answer = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x:x[2])
    for a, b, c in costs:
        if find(a) != find(b):
            union(a,b)
            answer += c
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))