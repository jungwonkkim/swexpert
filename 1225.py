#1225. [S/W 문제해결 기본] 7일차 - 암호생성기


for test_case in range(1, 11):
    n = int(input())
    num_list = list(map(int, input().split()))        
    while True:
        for i in range(1,6):
            num_list[0]-=i
            if num_list[0]<=0:
                num_list[0] = 0
                num_list = [num_list[1],num_list[2], num_list[3], num_list[4], num_list[5], num_list[6], num_list[7], num_list[0]]
                break
            else:
                num_list = [num_list[1],num_list[2], num_list[3], num_list[4], num_list[5], num_list[6], num_list[7], num_list[0]]
        
    print(f'#{n}', end = ' ')
    for i in range(8):
        print(num_list[i], end = ' ')
    print()
        