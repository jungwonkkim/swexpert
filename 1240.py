#1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
password_dict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101': 3, '0100011':4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111':8, '0001011':9}
def decoding(string):
    if string not in password_dict.keys():
        return -1
    else:
        return password_dict[string]


T = int(input())

for test_case in range(1, T + 1):
    row, column = map(int, input().split())
    password_list = []
    num_list = [[] for _ in range(row)]
    for i in range(row):
        num_list[i] = input()
    for num in num_list:
        if '1' not in num:
            continue
        else:
            num_str = num
            break
    for j in range(column-1,-1,-1):
        if num_str[j] =='1':
            password= num_str[j-55:j+1]
            break
    for k in range(8):
        temp = decoding(password[7*k:7*k+7])
        password_list.append(temp)
    if -1 not in password_list:
        if ((password_list[0]+password_list[2]+password_list[4]+password_list[6]) * 3 + password_list[1]+password_list[3]+password_list[5] + password_list[7]) % 10 !=0 :
            result = 0
        else:
            result = sum(password_list)
    else:
        result = 0
    print('#{} {}'.format(test_case, result))