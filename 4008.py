def calculate(num, idx):
    global min_val
    global max_val
    if idx == N:
        if min_val > num:
            min_val = num
        if max_val < num:
            max_val = num
            return
    else:
        if calculator[0] > 0:
            calculator[0] -=1
            calculate(num + numbers[idx], idx+1)
            calculator[0] += 1
        if calculator[1] > 0:
            calculator[1] -= 1
            calculate(num-numbers[idx], idx+1)
            calculator[1] +=1
        if calculator[2] > 0:
            calculator[2] -= 1
            calculate(num * numbers[idx], idx+1)
            calculator[2] += 1
        if calculator[3] > 0 and numbers[idx] != 0:
            calculator[3] -=1
            if num < 0 and num%numbers[idx]!=0:
                calculate(num//numbers[idx]+1, idx+1)
            else:
                calculate(num//numbers[idx], idx+1)
            calculator[3] +=1


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    calculator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_val = -100000001
    min_val = +100000001
    calculate(numbers[0], 1)
    print('#{} {}'.format(test_case, max_val - min_val))
