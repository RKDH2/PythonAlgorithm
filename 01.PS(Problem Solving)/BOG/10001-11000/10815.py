import sys

my_n = int(input())
my_l = set(map(int, sys.stdin.readline().split()))  # (6, 3, 2, 10, -10)

num_n = int(input())
num_l = list(map(int, sys.stdin.readline().split()))  # [10, 9, -5, 2, 3, 4, 5, -10]

for i in num_l:
    if i in my_l:
        print(1, end=" ")
    else:
        print(0, end=" ")
