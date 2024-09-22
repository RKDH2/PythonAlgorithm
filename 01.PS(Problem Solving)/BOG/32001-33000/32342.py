n = int(input())

result = []

for _ in range(n):
    s = input()
    count = 0
    for i in range(len(s) - 2):
        if s[i:i + 3] == "WOW":  # [0:2] -> [1:3] # i = 0 일때 i + 3은 0+3=3이니까 3전까지인 0,1,2까지
            count += 1
    result.append(count)

for i in result:
    print(i)
