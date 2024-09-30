# 재귀 함수 & 재귀 호출 사용
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

N = int(input())

print(factorial(N))
