n = int(input())
for i in range(n):
    stack = []
    a = input()
    for j in a:
        if j == "(":
            stack.append(j)
        elif j == ")": # 짝이 맞다면
            if stack:
                stack.pop() # 마지막 ( 지우기
            else: # 처음부터 ) 일 경우 바로 NO 출력 후 종료
                print("NO")
                break
    else: # 내부 for문이 끝나면 실행
        if not stack:
            print("YES")
        else:
            print("NO")
