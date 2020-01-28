#2817. 부분 수열의 합

def summaking(arr):
    result_list = [0]
    for i in arr:
        temp_list = []
        for result in result_list:
            temp_list.append(i+result)
        result_list +=temp_list
    return result_list

T = int(input())
for test_case in range(1, T + 1):
    N , K = map(int, input().split())
    num_list = list(map(int, input().split()))
    counter = 0
    result = summaking(num_list)
    for res in result:
        if res == K:
            counter +=1
    print(f'#{test_case} {counter}')