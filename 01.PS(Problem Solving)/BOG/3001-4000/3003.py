import sys

l = list(map(int, sys.stdin.readline().split())) # 0 1 2 2 2 7
chess = [1, 1, 2, 2, 2, 8]

r = [mych - ch for ch, mych in zip(l, chess)]

print(" ".join(map(str, r)))
