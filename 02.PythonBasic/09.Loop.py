i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)

array = [9, 8, 7, 6, 5]

for x in array:
    print(x)

for i in range(1, 10):
    result += 1

print(result)

for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i

print(result)

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

cheathing_student_list = {2, 4}

for i in range(5):
    if i + 1 in cheathing_student_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")
