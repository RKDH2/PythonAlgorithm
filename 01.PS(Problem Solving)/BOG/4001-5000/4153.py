import sys

while True:
    num = list(map(int, sys.stdin.readline().split()))
    if sum(num) == 0:
        break
    max_num = max(num)
    num.remove(max_num)
    if num[0]**2 + num[1]**2 == max_num**2:
        print("right")
    else:
        print("wrong")
