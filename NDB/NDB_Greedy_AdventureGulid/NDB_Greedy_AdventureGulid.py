n = map(int, input().split())
m = list(map(int, input().split()))
m.sort()
count = 0

while True:
    if len(m) == 0 | len(m) < m[len(m)-1]:
        break
    for i in range(m[len(m)-1]-1):
        m.pop(i)
    m.pop(len(m)-1)
    count += 1

print(count)