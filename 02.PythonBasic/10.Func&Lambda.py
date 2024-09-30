def add(a, b):
    return a + b


print(add(3, 7))


def subtract(a, b):
    return a - b


print(subtract(3, 7))

a = 0


def func():
    global a  # global 키워드를 사용하면 지역변수가 아닌 함수 바깥에 선언된 a 변수 사용
    a += 1


for i in range(10):
    func()

print(a)

array = [1, 2, 3, 4, 5]


def func():
    array.append(6)
    print(array)


func()
print(array)


def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var


a, b, c, d = operator(7, 3)
print(a, b, c, d)

#  Lambda 문법
print((lambda a, b: a + b)(3, 7))

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))  # 간단하게 Lambda 로 표현하기

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))
