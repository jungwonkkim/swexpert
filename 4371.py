#4371. 항구에 들어오는 배

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    num_list = []
    for i in range(n):
        num_list.append(int(input())-1)
    num_boolean = [True] * n
    for i in range(1, len(num_list)-1):
        for j in range(i+1, len(num_list)):
            if num_list[j] %num_list[i] ==0:
                num_boolean[j] = False
    counter = num_boolean[1:].count(True)
    print(f'#{test_case} {counter}')
                
    