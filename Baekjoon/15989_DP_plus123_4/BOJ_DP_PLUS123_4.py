t = int(input())
list = []
for i in range(t):
    list.append(int(input()))

dp = [0] * 10001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, max(list)+1):
    dp[i] = dp[i-1] + (dp[i-2] - dp[i-3])
    if i % 3 == 0:
        dp[i] += 1


for i in list:
    print(dp[i])