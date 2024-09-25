import sys

input = sys.stdin.readline

while True:
    num = input().strip()

    if num == "0":
        break

    l = [int(n) for n in num]
    count = 0

    for i in range(len(l) // 2):
        if l[i] == l[-(i + 1)]:
            count += 1

    if len(l) // 2 == count:
        print("yes")
    else:
        print("no")
