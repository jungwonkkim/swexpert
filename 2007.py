#2007 패턴 마디의 길이

T = int(input())

for test_case in range(1, T + 1):
    my_str = input()
    spec_str = my_str[8:10]
    spec_count = my_str[0:8].count(spec_str)
    result = 0
    if spec_count ==0:
        if my_str[0:9] ==my_str[10:19]:
            result = 10
        else:
            result = 9
    elif spec_count ==1:
        if my_str[0:2]==my_str[5:7]:
            result = 5
        elif my_str[0:2] == my_str[6:8]:
            result = 6
        else:
            result = 7
    elif spec_count ==2:
        if my_str[0:2]==my_str[3:5]:
            result = 3
        else:
            result = 4
    else:
        if my_str[0]==my_str[1]:
            result = 1
        else :
            result = 2
    print(f'#{test_case} {result}')
  