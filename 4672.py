#4672. 수진이의 팰린드롬
T = int(input())

for test_case in range(1, T+1):
    str_list = input()
    res = 0
    char_count = {}
    for char in str_list:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    for key in char_count:
        value = char_count[key]
        res += value*(value+1)//2

    print('#{} {}'.format(test_case, res))
