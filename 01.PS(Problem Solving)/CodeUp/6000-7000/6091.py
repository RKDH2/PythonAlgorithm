# 6091
a, b, c = map(int, input().split())
d = 1

while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1

print(d)

# ---------------- 다른 방법

# 6091
a, b, c = map(int, input().split())
d = 1
while True:
    if d % a == 0 and d % b == 0 and d % c == 0:
        break
    else:
        d += 1
print(d)

n = int(input())  # 10
a = map(int, input().split())  # [1 3 2 2 5 6 7 4 5 9]

print(a)

# 6092
n = int(input())  # 10

a = list(map(int, input().split()))  # [1 3 2 2 5 6 7 4 5 9]

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1  # 예) a가 1이면 a[1] = 3이기 때문에 d[3]번째에 +1 카운트 추가

for i in range(1, 24):
    print(d[i], end=' ')  # 1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
