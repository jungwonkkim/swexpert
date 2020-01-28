#3282. 0/1 Knapsack

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
    N, K = map(int, input().split())
    max_val = 0
    v_list = []
    c_list = []
    for i in range(N):
        v, c= map(int,input().split())
        v_list.append(v)
        c_list.append(c)
    v_list = summaking(v_list)
    c_list = summaking(c_list)
    for i in range(len(v_list)):
        if v_list[i] <= K:
            if c_list[i]>max_val :
                max_val = c_list[i]
    print('#{} {}'.format(test_case, max_val))


    