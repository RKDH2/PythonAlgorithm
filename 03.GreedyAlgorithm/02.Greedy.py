n, m, k = map(int, input().split())

data = list(map(int, input().split()))

# 작은 순으로 정렬
data.sort()

# 가장 큰 수 가져오기
first_data = data[n - 1]
second_data = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first_data
        m -= 1
    if m == 0:
        break
    result += second_data
    m -= 1

print(result)

# -------------------------------------

# n : 배열 크기, m : 숫다가 더해지는 횟수, k : 특정 인덱스 연속 가능 횟수
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 정렬

first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k  # 예) 결과 : 6

# 반복되고 남은 더하기 횟수
count += m % (k + 1)  # 예) 남은 횟수 없음 : 0

result = 0
result += count * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기 (더해지는 횟수 - count)

print(result)
