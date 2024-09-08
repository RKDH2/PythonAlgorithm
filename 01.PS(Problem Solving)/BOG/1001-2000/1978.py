import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
count = 0

for num in l:
    flag = True
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            count += 1

print(count)
