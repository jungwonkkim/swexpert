# 6959. 이상한 나라의 덧셈게임

T = int(input())

for test_case in range(1, T+1):
    stack = list(map(int, input()))
    count = 0
    while len(stack)>1:
        a = stack.pop()
        b = stack.pop()
        new_number = a+b
        if a+b<10:
            stack.append(new_number)
        else:
            stack.append(new_number//10)
            stack.append(new_number%10)
        count+=1

    if count%2:
        winner = 'A'
    else:
        winner = 'B'
    print('#{} {}'.format(test_case, winner))