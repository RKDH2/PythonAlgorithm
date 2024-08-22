n, m = map(int, input().split())

result = 0

for i in range(n):
    # 행에 넣을 수를 입력받기
    data = list(map(int, input().split()))
    # 행에서 가장 작은 데이터 가져오기
    min_value = min(data)
    # 이전에 가장 작은 값과 이번에 가장 작은 값과 비교하고 더 작은 값을 result에 넣기
    result = max(result, min_value)

print(result)
