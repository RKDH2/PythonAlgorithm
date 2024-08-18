# 정수 입력받기
N = int(input())  # 수의 개수 N개를 입력받음
numbers = []  # 숫자들을 담을 리스트

# N개의 수 입력받기
for i in range(N):
    num = int(input())  # N개의 수만큼 반복해서 수를 입력받기
    numbers.append(num)  # 리스트에 추가

numbers.sort()  # 낮은 순으로 정렬

for num in numbers:
    print(num)
