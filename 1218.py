#1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기

for test_case in range(1, 11):
    length = int(input())
    text = input()
    stack = []
    result =1
    for char in text:
        if result == 0:
            break
        if char =='(' or char=='{' or char =='[' or char =='<':
            stack.append(char)
        elif char ==')':
            if stack and stack.pop() == '(':
                continue
            else:
                result = 0
        elif char == '}':
            if stack and stack.pop() == '{':
                continue
            else:
                result = 0
        elif char == ']':
            if stack and stack.pop() == '[':
                continue
            else:
                result = 0
        elif char =='>':
            if stack and stack.pop() == '<':
                continue
            else:
                result = 0
    if stack:
        result = 0
    print('#{} {}'.format(test_case,result))
