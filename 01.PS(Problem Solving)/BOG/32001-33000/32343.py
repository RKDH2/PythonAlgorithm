n = int(input())
a, b = map(int, input().split())

x = []
for i in range(1 << n):
    if bin(i).count('1') == a:
        x.append(i)

y = []
for i in range(1 << n):
    if bin(i).count('1') == b:
        y.append(i)

max_v = 0
for j in x:
    for k in y:
        max_v = max(max_v, j ^ k)

print(max_v)
