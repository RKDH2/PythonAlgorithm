n = int(input())
# 1 -> 6 -> 12 -> 18 # 6개씩 증가
total = 1
block = 6
count = 1  # 시작 지점부터 카운트

while total < n:
    total += block
    count += 1
    block += 6

print(count)
