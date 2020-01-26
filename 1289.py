#1289. 원재의 메모리 복구하기

T = int(input())

for test_case in range(1, T + 1):
    num_list = list(input())
    state_list = [ 0 for _ in range(len(num_list))]
    counter = 0
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    for i in range(len(num_list)):
        if state_list == num_list:
            break
        else:
            if num_list[i] != state_list[i]:
                counter+=1
                for j in range(i, len(num_list)):
                    state_list[j] = num_list[i]              
    print(f'#{test_case} {counter}')