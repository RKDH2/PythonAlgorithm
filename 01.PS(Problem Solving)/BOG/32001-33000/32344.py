import sys
input = sys.stdin.readline

r, c = map(int, input().split())
n = int(input())

art = {}

for _ in range(n):
    a, v, h = map(int, input().split())
    if a not in art:
        art[a] = []
    art[a].append((v, h))

max_area = 0
art_id = None

for a in art:
    rows = [pos[0] for pos in art[a]]
    cols = [pos[1] for pos in art[a]]
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)
    area = (max_row - min_row + 1) * (max_col - min_col + 1)
    if area > max_area or (area == max_area and (art_id is None or a < art_id)):
        max_area = area
        art_id = a

print(art_id, max_area)
