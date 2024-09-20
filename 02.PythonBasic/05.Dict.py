data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("사과가 존재한다.")

# 키 데이터만 가져오는 keys() 함수 사용 가능
print(data.keys())
# 값 데이터만 가져오는 values() 함수 사용 가능
print(data.values())

for key in data.keys():
    print(key)

b = {
    '홍길동': 97,
    '이순신': 98,
}

print(b)
print(b['이순신'])
key_list = list(b.keys())
print(key_list)
