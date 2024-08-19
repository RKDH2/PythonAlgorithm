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
