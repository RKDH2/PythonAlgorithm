import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for i in range(n)]
coins.sort(reverse=True)

count = 0

for coin in coins:
    count += k // coin
    k %= coin

print(count)
