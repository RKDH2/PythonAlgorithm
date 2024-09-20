x = 15

if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x >= 30")
elif x >= 20:
    print("x >= 20")
elif x >= 10:
    print("x >= 10")
else:
    print("x < 10")

if True or False:
    print("Yes")

if True and False:
    print("Yes")

a = 15

if a <= 20 and a >= 0:
    print("Yes")

l = [1, 2, 3]
x = 2

# 리스트 안에 x가 들어가 있을 때 참(True)이다.
if x in l:
    print("Yes")

# 문자열 안에 x가 들어가 있지 않을 때 참(True)이다.
if x not in l:
    print("Yes")

score = 85

if score >= 80:
    pass
else:
    print("성적이 80점 미만입니다.")

# 참(True) 값이 왼쪽 거짓(False)일 때 오른쪽 값이 들어감.
result = "Success" if score >= 80 else "Fail"
print(result)
