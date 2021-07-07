n , m = map(int, input().split())
list_home = [int(input()) for _ in range(n)]
list_home.sort()

min = 1
s = len(list_home)
max = list_home[s-1] - list_home[0]
answer = 0
while max >= min:
    tmp = 0
    count = 1
    for i in range(1,s):
        mid = (min + max) // 2
        if mid <= list_home[i] - list_home[tmp]:
            count += 1
            tmp = i

    if count >= m:
        answer = mid
        min = mid + 1
    else:
        max = mid -1

print(answer)