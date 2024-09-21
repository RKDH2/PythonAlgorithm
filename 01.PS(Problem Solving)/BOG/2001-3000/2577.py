a = int(input())
b = int(input())
c = int(input())
total = list(str(a * b * c))

for i in range(10):
    print(total.count(str(i)))

# 다른 방법
total = 1

for _ in range(3):
    total *= int(input())

total = list(str(total))

for i in range(10):
    print(total.count(str(i)))
