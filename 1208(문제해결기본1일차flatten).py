#1208 flatten 15분 08초

for test_case in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))
    for i in range (dump):
        if max(box_list) - min(box_list)<=1:
            break
        else :  
            box_list.sort()
            box_list[0]+=1
            box_list[-1]-=1
    result = max(box_list) - min(box_list)
    print(f'#{test_case} {result}')