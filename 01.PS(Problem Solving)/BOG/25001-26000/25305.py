a, b = map(int, input().split())
c = list(map(int, input().split()))

c.sort(reverse=True)
d = c[b - 1]

print(d)
