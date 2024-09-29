a, b , v = map(int, input().split())

days = (v-b-1) // (a-b) + 1 # 마지막 날에 도달해야 하는 높이, 마지막 날에는 미끄러지지 않으므로 (B)를 빼준다.

print(days)
