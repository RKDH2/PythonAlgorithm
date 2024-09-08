import sys

n = int(sys.stdin.readline())
a = [0]*(10001)

for i in range(n):
    s = int(sys.stdin.readline())
    a[s]+=1
for i in range(1, len(a)):
    for j in range(a[i]):
        print(i)
