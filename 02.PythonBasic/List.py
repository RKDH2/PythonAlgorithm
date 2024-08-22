a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

a[8] = 10
print(a[8])

print(a[4])
print(a[2:5])
print(a[:3])

print(a[-2])
print(a[-6])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 리스트 컴프리헨션
# 대괄호 속 조건문과 반복문을 넣어 리스트를 한줄로 초기화 할 수 있다.
array = [i for i in range(20)]
print(array)

array = [i for i in range(20) if i % 2 == 1]
print(array)

n = 4
m = 3
array = [[0] * m for i in range(n)]
print(array)

# append() : 리스트에 원소를 하나 삽입
# sort() : 오름차순으로 정렬
# sort(reverse = True) : 내림차순으로 정렬
# insert(index, value) : 특정 인덱스에 요소를 삽입
# remove() : 리스트에 첫 번째로 나타나는 값이 지정한 요소와 같으면 삭제
# count(value) : vlaue가 몇 개 있는지
# pop() : 마지막 요소 삭제
# clear() : 모든 요소 삭제
