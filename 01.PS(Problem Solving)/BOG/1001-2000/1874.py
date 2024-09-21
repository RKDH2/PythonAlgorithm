import sys

input = sys.stdin.readline

n = int(input())
l = []  # 받아올 수열
stack = []  # 현재 저장된 정수
result = []  # 결과 '+' 또는 '-' 저장 리스트
current = 1  # 저장할 정수
impossible = True

for _ in range(n):
    l.append(int(input()))  # 수열 받아오기

for num in l:  # 4, 3, 6, 8, 7, 5, 2, 1
    while current <= num:  # 받아온 수열과 작거나 같아질 때까지 반복
        stack.append(current)  # 조건 만족할 때까지 정수 추가
        result.append('+')  # '+' 결과 값 하나씩 저장
        current += 1  # 정수를 1씩 늘리기
    if stack and stack[-1] == num:  # 만약 스택이 비어있지 않고 최상단 요소가 num과 같을경우
        stack.pop()  # 정수 제거
        result.append('-')  # '-' 결과 값 하나씩 저장
    else:  # 만약 같은 수가 있어있는 등 불가능한 경우
        impossible = False  # 불가 판정 내리기
        break  # for문 멈추기

if impossible:  # 불가 판정이 아닌경우
    for i in result:  # 결과 '+' 또는 '-'를 받아온 reuslt를 출력
        print(i)
else:  # 불가 판정을 받은경우
    print("NO")
