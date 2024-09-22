import sys

n = int(sys.stdin.readline().strip())
count = [0] * 10
num = 1

while n > 0:
    while n % 10 != 9:
        for i in str(n):
            count[int(i)] += num
        n -= 1

    if n < 10:
        for j in range(n + 1):
            count[j] += num
        count[0] -= num
        break
    else:
        for k in range(10):
            count[k] += (n // 10 + 1) * num  # 0 ~ 9까지 각 숫자가 (n // 10 + 1)번씩 등장

    count[0] -= num  # 0으로 시작하는 숫자가 없으므로 0의 카운트를 조정
    num *= 10
    n //= 10

print(*count)
