import sys
input = sys.stdin.readline

n = int(input()) # 23
sizes = list(map(int, input().split())) # 3 1 4 1 5 9
ts, pen = map(int, input().split()) # 5 7

ts_bundle = 0

for size in sizes: # 3 1 4 1 5 9
    if size % ts == 0:
        ts_bundle += size // ts
    else:
        ts_bundle += size // ts + 1

pen_bundle = n // pen
addPen = n % pen

print(ts_bundle)
print(pen_bundle, addPen)
