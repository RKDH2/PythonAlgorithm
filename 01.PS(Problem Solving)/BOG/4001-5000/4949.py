def is_balanced(s):
    stack = []
    for char in s:
        if char in "([":  # 왼쪽 괄호를 만나면 스택에 추가
            stack.append(char)
        elif char in ")]":  # 오른쪽 괄호를 만나면 스택에서 제거
            if not stack:  # 스택이 비어 있으면 균형이 맞지 않음
                return False
            top = stack.pop()
            if char == ")" and top != "(":  # 짝이 맞지 않으면 균형이 맞지 않음
                return False
            if char == "]" and top != "[":  # 짝이 맞지 않으면 균형이 맞지 않음
                return False
    return not stack  # 스택이 비어 있으면 균형이 맞음


while True:
    line = input().rstrip()
    if line == ".":
        break
    if is_balanced(line):
        print("yes")
    else:
        print("no")

# --------------------------------------------
while True:
    word = input()
    stack = []
    if word == ".":
        break

    for w in word:
        if w == "(" or w == "[":
            stack.append(w)
        elif w == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(w)
                break
        elif w == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(w)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")