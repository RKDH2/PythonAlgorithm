import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            max_num = cards[i] + cards[j] + cards[k]
            if max_num <= m:
                result = max(result, max_num)

print(result)
