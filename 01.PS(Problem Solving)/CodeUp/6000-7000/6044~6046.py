# 6044
a, b = map(int, input().split())
c1 = a + b
print(c1)
c2 = a - b
print(c2)
c3 = a * b
print(c3)
c4 = a // b
print(c4)
c5 = a % b
print(c5)
c6 = float(a) / float(b)
print(format(c6, ".2f"))

# 6045
a, b, c = map(int, input().split())
r = a + b + c
r2 = r / 3
print(r, f'{r2:.2f}')  # f-string 방법

# 6046
n = int(input())
print(n << 1)  # 2배 값
