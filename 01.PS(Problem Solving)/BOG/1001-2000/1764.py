import sys

input = sys.stdin.readline

n, m = map(int, input().split())
name_list_1 = []
name_list_2 = []

for i in range(n + m):
    if i < n:
        name_list_1.append(input().strip())
    else:
        name_list_2.append(input().strip())

set_1, set_2 = set(name_list_1), set(name_list_2)

crossing = sorted(set_1 & set_2)

print(len(crossing))
for name in crossing:
    print(name)
