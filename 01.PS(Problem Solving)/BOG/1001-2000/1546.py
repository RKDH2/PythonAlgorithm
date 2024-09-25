import sys

input = sys.stdin.readline

n = int(input())

score = list(map(int, input().split()))

max_score = max(score)
temp_num = [(s / max_score) * 100 for s in score]
result = sum(temp_num) / n
print(result)
