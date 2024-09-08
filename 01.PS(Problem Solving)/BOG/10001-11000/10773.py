import sys

n = int(sys.stdin.readline())
stack = []
result = 0
for i in range(n):
    s = int(sys.stdin.readline())
    if s != 0:
        stack.append(s)
    else:
        stack.pop()
for i in stack:
    result += i
print(result)
