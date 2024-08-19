# 6073
n = int(input())
for i in range(n - 1, -1, -1):
    print(i)

# 6074
c = ord(input())

t = ord('a')
while t <= c:
    # 값 출력 후 공백 문자 출력 (end=' ')
    print(chr(t), end=' ')
    t += 1
