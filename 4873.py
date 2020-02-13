#4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

T = int(input())

for test_case in range(1, T+1):
    text = input()
    test_list = []
    for char in text:
        if test_list == []:
            test_list.append(char)
        else:
            if char == test_list[-1]:
                test_list.pop()
            else:
                test_list.append(char)

    print('#{} {}'.format(test_case,len(test_list)))