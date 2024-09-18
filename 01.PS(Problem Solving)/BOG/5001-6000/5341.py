import sys

input = sys.stdin.readline
num = []
while True:
    n = int(input())
    if n == 0:
        break
    num.append(n)

for n in num:
    total = n * (n + 1) // 2
    print(total)
