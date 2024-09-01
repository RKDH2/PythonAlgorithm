import sys

n = int(input())

l = list(map(int, sys.stdin.readline().split()))  # l = [2, 4, -10, 4, -9]

sortedList = sorted(list(set(l)))  # sortedList = [-10, -9, 2, 4]
dcn = dict(zip(sortedList, list(range(len(sortedList)))))  # {-10: 0, -9: 1, 2: 2, 4: 3}

for i in l:
    print(dcn[i])  # 예) l이 2라면 dcn에 있는 key 값이 2인 수를 찾고 value 값을 가져온다.

# 최적화 코드
import sys

n = int(input())
l = list(map(int, sys.stdin.readline().split()))

sortedList = sorted(set(l))
dcn = {val: idx for idx, val in enumerate(sortedList)}

for i in l:
    print(dcn[i], end=" ")
