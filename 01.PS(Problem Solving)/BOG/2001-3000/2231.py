n = int(input())  # 216
isTotal = False

for i in range(1, n):
    total = 0
    num = str(i)
    for j in num:  # num = 198 이라면
        total += int(j)  # 결과 값 : 18 += +1 -> +9 -> +8
    total += int(num)  # 결과 값 : 216 <- 18 += 198
    if total == n:  # 216 == 216 같을 경우
        isTotal = True
        break

if isTotal:
    print(int(num))
else:
    print(0)
