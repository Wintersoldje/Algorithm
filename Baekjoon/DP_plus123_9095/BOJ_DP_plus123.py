t = int(input())

num = []
for i in range(t):
    num.append(int(input()))
dp = [1,2,4]

for i in range(3, max(num)):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in num:
    print(dp[i-1])