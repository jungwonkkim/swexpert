T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    temp_list = list(map(int, input().split()))
    su_list = []
    am_list = []
    bolt_list = []
    for i in range(n*2):
        if i % 2 :
            am_list.append(temp_list[i])
        else:
            su_list.append(temp_list[i])
    for bolt in range(n):
        if su_list[bolt] not in am_list:
            start_point = bolt
            bolt_list.append(su_list.pop(bolt))
            bolt_list.append(am_list.pop(bolt))
            break
        
    while len(su_list) != 0 :
        for bolt in range(len(su_list)):
            if su_list[bolt] == bolt_list[-1]:
                bolt_list.append(su_list.pop(bolt))
                bolt_list.append(am_list.pop(bolt))
                break
    bolt_list = [str(bolt) for bolt in bolt_list]
    bolt_ans = ' '.join(bolt_list)
    print('#{} {}'.format(test_case, bolt_ans))
        
                
            
