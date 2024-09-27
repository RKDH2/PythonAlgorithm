import sys

input = sys.stdin.readline

dp = [[1, 0], [0, 1]] + [[0, 0] for i in range(39)] # 예 : [0을 1번 호출, 1을 0번 호출] -> [1, 0]

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

T = int(input())

for i in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])
