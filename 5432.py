#5432. 쇠막대기 자르기

T = int(input())

for test_case in range(1, T+1):
    steel = input()
    c_count = 0
    left_count = 0
    right_count = 0
    laser_count = 0
    for idx, s in enumerate(steel):
        if s =='(':
            left_count+=1
        else:
            if steel[idx-1]== '(':
                c_count +=1
                right_count += 1
                laser_count += (left_count-right_count)
            else:
                right_count+=1
    laser_count += left_count - c_count
    print('#{} {}'.format(test_case,laser_count))
