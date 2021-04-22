from collections import deque

n, m, k, x = map(int, input().split())
list_line = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    list_line[a].append(b)

# 모든 도시에 대한 최단거리 최소화
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for nextnode in list_line[now]:
        if distance[nextnode] == -1:
            distance[nextnode] = distance[now] + 1
            q.append(nextnode)
        print(distance)
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)

