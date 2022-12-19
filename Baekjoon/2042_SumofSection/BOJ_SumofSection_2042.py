import math

n, m, k = map(int, input().split())
list_num = []
list_command = []
for i in range(n):
    list_num.append(int(input()))
for i in range(m+k):
    tmp = list(map(int, input().split()))
    list_command.append(tmp)

num = (pow(2, math.ceil(math.log(n, 2))+1))-1
list_tree = [0] * num

def init(start, end, node):
    if start == end:
        list_tree[node] = list_num[start]
        return list_tree[node]
    mid = (start + end) // 2
    list_tree[node] = init(start, mid, node*2) + init(mid + 1, end, node * 2 + 1)
    return list_tree[node]

def update(start, end, node, index, diff):
    if index < start or end < index:
        return
    list_tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, diff)
    update(mid + 1, end, node * 2 + 1, index, diff)

def summit(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return list_tree[node]
    mid = (start + end) // 2
    return summit(start, mid, node * 2, left, right) + summit(mid + 1, end, node * 2 + 1, left, right)


init(0, n-1, 1)

for i in list_command:
    if i[0] == 1:
        i[1] -= 1
        diff = i[2] - list_num[i[1]]
        list_num[i[1]] = i[2]
        update(0, n-1, 1, i[1], diff)
    else:
        print(summit(0, n-1, 1, i[1] - 1, i[2] - 1))
