parent = []
def find(target):
    if target == parent[target]:
        return target
    return find(parent[target])

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[a] = pb
    else:
        parent[b] = pa

def solution(n, computers):
    answer = 0
    global parent
    for i in range(n):
        parent.append(i)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                union(i,j)
    list_answer = []
    for i in range(n):
        list_answer.append(find(parent[i]))
    answer = len(set(list_answer))
    return answer
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# parent = []
# def find(target):
#     if target == parent[target]:
#         return target
#     return find(parent[target])
#
# def union(a, b):
#     pa = find(a)
#     pb = find(b)
#
#     if pa < pb:
#         parent[a] = pb
#     else:
#         parent[b] = pa
#
# def solution(n, computers):
#     global parent
#     parent = [0] * n
#     for i in range(n):
#         parent[i] = i
#     for i in range(len(computers)):
#         for j in range(len(computers)):
#             if i == j:
#                 continue
#             if computers[i][j] == 1:
#                 union(i, j)
#     list_num = []
#     for i in range(n):
#         list_num.append(find(parent[i]))
#     answer = len(set(list_num))
#
#     return answer