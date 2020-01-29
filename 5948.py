#5948. 새샘이의 7-3-5 게임

T = int(input())
for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    mul_list = []
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                result = num_list[i] + num_list[j] + num_list[k]
                mul_list.append(result)
    mul_list.sort()
    mul_list = list(set(mul_list))
    print(f'#{test_case} {mul_list[-5]}')
