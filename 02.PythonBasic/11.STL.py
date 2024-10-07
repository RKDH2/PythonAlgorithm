result = sum([1, 2, 3, 4, 5])
print(result)

min_result = min([1, 2, 3, 4, 5])
max_result = max([1, 2, 3, 4, 5])
print(min_result, max_result)

result = eval("(3+5)*7")
print(result)

result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)

from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
print(result)

from itertools import product

data = ['A', 'B', 'C']

result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기
print(result)

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # 'blue' 등장한 횟수 출력
print(counter['green'])  # 'green' 등장한 횟수 출력
print(dict(counter))  # 사전 자료형으로 변환

import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14))  # 최대 공약수(GCD) 계산
print(lcm(21, 14))  # 최소 공배수(LCM) 계산
