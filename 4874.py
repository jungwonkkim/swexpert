#4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth

def calculator(arr):
    newstack = []
    for num in arr :
        if num == '.':
            if len(newstack) ==1:
                return newstack[0]
            else:
                return 'error'
        if num == '+':
            if len(newstack)>=2:
                cal1 = newstack.pop()
                cal2 = newstack.pop()
                newstack.append(cal1+cal2)
            else:
                return 'error'
        elif num == '*':
            if len(newstack)>=2:
                cal1 = newstack.pop()
                cal2 = newstack.pop()
                newstack.append(cal1*cal2)
            else:
                return 'error'
        elif num == '/':
            if len(newstack)>=2:
                cal1 = newstack.pop()
                cal2 = newstack.pop()
                newstack.append(int(cal2/cal1))
            else:
                return 'error'
        elif num == '-':
            if len(newstack)>=2:
                cal1 = newstack.pop()
                cal2 = newstack.pop()
                newstack.append(cal2-cal1)
            else:
                return 'error'
        else:
            newstack.append(int(num))
    return 'error'

T = int(input())

for test_case in range(1, T + 1):
    num_list = list(input().split())
    result = calculator(num_list)
    print('#{} {}'.format(test_case, result))