n = int(input())
list_stair = []
for i in range(n):
    tmp = int(input())
    list_stair.append(tmp)
result = 0
dp = []
if n == 1:
    print(list_stair[0])
elif n == 2:
    print(list_stair[0] + list_stair[1])
else:
    dp.append(list_stair[0])
    dp.append(max(dp[0] + list_stair[1], list_stair[1]))
    dp.append(max(dp[0] + list_stair[2], list_stair[1] + list_stair[2]))
    for i in range(3,n):
        dp.append(max(list_stair[i] + list_stair[i-1] + dp[i-3], list_stair[i] + dp[i-2]))

    print(dp[len(list_stair)-1])
