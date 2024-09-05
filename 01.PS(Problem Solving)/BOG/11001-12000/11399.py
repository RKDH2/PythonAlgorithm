import sys
n = int(sys.stdin.readline().strip())
z = list(map(int, sys.stdin.readline().strip().split()))
z.sort()
r = 0
c = 0
for i in z:
    c += i
    r += c

print(r)
