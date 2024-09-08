import sys

h, m = map(int, sys.stdin.readline().split())
oven = int(input())

h += oven // 60
m += oven % 60

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h, m)
