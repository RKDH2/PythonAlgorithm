import sys

n, x = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
s = []
for i in range(n):
    if l[i] < x:
        s.append(l[i])
for j in s:
    print(j, end=" ")
