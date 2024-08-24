# 6078
n = ord('q')
c = ord(input())
print(chr(c))
while c != n:
    c = ord(input())
    print(chr(c))

# 6079
n = int(input())
total = 0
i = 1

while total < n:
    total += i
    i += 1

print(i - 1)

# 6080
n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print(i + 1, j + 1)
    j = 0

# 6081
n = int(input(), 16)

for i in range(1, 16):
    print('%X' % n, '*%X' % i, '=%X' % (n * i), sep='')

# 6082
n = int(input())

for i in range(1, n + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("X", sep=' ')
    else:
        print(i, sep=' ')

# 6083
r, g, b = map(int, input().split())

count = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)

print(r * g * b)

# 6084
a, b, c, d = map(int, input().split())
total = a * b * c * d

byteTotal = total / 8
kbTotal = byteTotal / 1024
mbTotal = kbTotal / 1024

print("%0.1f MB" % mbTotal)

# 6085
a, b, c = map(int, input().split())

totalBit = a * b * c

totalByte = totalBit / 8
totalKb = totalByte / 1024
totalMb = totalKb / 1024

print("%0.2f MB" % totalMb)
