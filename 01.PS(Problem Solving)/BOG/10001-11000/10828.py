import sys

n = int(sys.stdin.readline().strip())
stack = []
for i in range(n):
    l = sys.stdin.readline().split()

    if len(l) == 1:
        com = l[0]
        if com == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif com == "size":
            print(len(stack))
        elif com == "empty":
            print(1 if not stack else 0)
        elif com == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
    elif len(l) == 2:
        com = l[0]
        val = int(l[1])
        if com == "push":
            stack.append(val)
