n, m = map(int, input().split())
INF = int(1e9)
list = [[INF] * n for i in range(n)]
# for i in range(n):
#     list[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    list[a-1][b-1] = 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if list[j][i] + list[i][k] < list[j][k]:
                list[j][k] = list[j][i] + list[i][k]
answer = 0
# print(list)
for i in range(n):
    count = 0
    for j in range(n):
        if list[i][j] != INF or list[j][i] != INF:
            count += 1
    if count == n-1:
        answer += 1

print(answer)


