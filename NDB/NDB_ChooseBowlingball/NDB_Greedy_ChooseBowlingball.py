n, m = map(int, input().split())
l = list(map(int, input().split()))
count = 0

for i in range(n-1):
    for j in range(i+1,n):
        #무게가 같을때는 pass
        if l[i] == l[j]:
            continue
        count += 1

print(count)