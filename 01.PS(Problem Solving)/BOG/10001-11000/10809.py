n = input()
en = "abcdefghijklmnopqrstuvwxyz"
l = []

for e in en:
    if e in n:
        print(n.index(e), end=" ")
    else:
        print(-1, end=" ")
