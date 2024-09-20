# 데이터 개수 입력
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 단순하게 공백 기준으로 구분해 3개의 입력만 받는 방법
a, b, c = map(int, input().split())
print(a, b, c)

import sys

# 입력을 빠르게 받기 (입력값이 많을 경우에 사용하기)
data = sys.stdin.readline().rstrip()
print(data)

a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

answer = 7
print("정답은 " + str(answer) + "입니다.")
print(f"정답은 {answer}입니다.")
