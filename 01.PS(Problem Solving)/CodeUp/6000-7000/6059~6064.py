# 6059
n = int(input())
n2 = ~n
print(n2)

# 6060
a, b = map(int, input().split())
c = a & b
print(c)

# 6061
a, b = map(int, input().split())
c = a | b
print(c)

# 6062
a, b = map(int, input().split())
c = a ^ b
print(c)

# 6063
a, b = map(int, input().split())
c = a if a >= b else b
print(c)

# 6064
a, b, c = map(int, input().split())
d = (a if a < b else b) if ((a if a < b else b) < c) else c
print(d)
