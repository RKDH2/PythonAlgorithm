import sys
n = int(input())
l = []
for i in range(n):
    (a, b) = sys.stdin.readline().split()
    l.append((int(a), b))
l.sort(key=lambda x: x[0])
for i in l:
    print(i[0], i[1])
