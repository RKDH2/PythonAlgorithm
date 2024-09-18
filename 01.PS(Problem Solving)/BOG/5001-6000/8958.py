import sys

input = sys.stdin.readline
n = int(input())
result = []
for i in range(n):
    l = input().strip()
    score = 0
    total = 0
    for s in l:
        if s == 'O':
            score += 1
            total += score
        else:
            score = 0
    result.append(total)

for i in result:
    print(i)
