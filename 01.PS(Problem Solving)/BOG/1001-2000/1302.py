import sys

dic = {}
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

v_max = max(dic.values())

l = []

for j in dic:
    if v_max == dic[j]:
        l.append(j)
l.sort()
print(l[0])
