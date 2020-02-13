# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

T= int(input())
for test_case in range(1, T + 1):
    test_str = input()
    stack = []
    result = 1
    for char in test_str:
        if result == 0:
            break
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                if stack.pop() == '{':
                    result = 0
            else:
                result = 0
        elif char == '{':
            stack.append(char)
        elif char == '}':
            if stack:
                if stack.pop() == '(':
                    result = 0
            else:
                result = 0
    if stack:
        result = 0
    print('#{} {}'.format(test_case, result))


