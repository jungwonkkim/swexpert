#1486. 장훈이의 높은 선반

def summaking(arr, i):
    global sum_set
    temp_set = {i for i in sum_set}
    for num in temp_set:
        sum_set.add(num + arr[i])

T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    height_list = list(map(int, input().split()))
    sum_set = {height_list[0],0}
    if N>=2:
        for a in range(1, len(height_list)):
            summaking(height_list,a)
    search = B
    while True:
        if search in sum_set:
            print('#{} {}'.format(test_case, search-B))
            break
        search +=1
