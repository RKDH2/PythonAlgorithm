array = []
for i in range(5):
    array.append(int(input()))

plus = sum(array) // 5
array.sort()

print(plus)
print(array[2])