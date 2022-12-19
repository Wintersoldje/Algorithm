n = int(input())
list_wine = [0] * 10000
for i in range(n):
    list_wine[i] = int(input())

dp = [0] * 10000
dp[0] = list_wine[0]
dp[1] = list_wine[0] + list_wine[1]
dp[2] = max(list_wine[2] + list_wine[1], list_wine[2] + dp[0], dp[1])
for i in range(3, n):
    dp[i] = max(list_wine[i] + dp[i-2], list_wine[i] + list_wine[i-1] + dp[i-3], dp[i-1])
print(max(dp))