import sys

input = sys.stdin.readline

n = int(input())
S = set()

for i in range(n):
    l = input().split()

    com = l[0]
    if len(l) > 1:
        x = int(l[1])

    if com == "add":
        S.add(x)
    elif com == "remove":
        S.discard(x)
    elif com == "check":
        if x in S:
            print(1)
        else:
            print(0)
    elif com == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif com == "all":
        S = set(range(1, 21))
    elif com == "empty":
        S.clear()
