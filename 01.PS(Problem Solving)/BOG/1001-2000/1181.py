import sys
n = int(input())
l = []
for i in range(n):
    s = sys.stdin.readline().strip()  # strip() 사용하지 않으면 입력 끝에 \n이 들어가기 떄문에 필수로 필요
    l.append(s)
result_1 = set(l)
result_2 = list(result_1)
result_2.sort(key=lambda word: (len(word), word))
for i in result_2:
    print(i)
