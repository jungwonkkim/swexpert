#3750. Digit sum
T = int(input())
result_list = []
for test_case in range(0, T):
    num_list = list(input())
    num_list = [int(num) for num in num_list]
    result = 0
    for num in num_list:
        result += num
        if result>=10:
            result-=9
    result_list.append(result)
    
for i in range(T):
    print(f'#{i+1} {result_list[i]}')