#4522 세상의 모든 팰린드롬
T = int(input())

for test_case in range(1, T + 1):
    text = input()
    if '?' in text:
        for i in range(len(text)//2):
            if text[i] != text[-1-i]:
                if text[i] != '?' and text[-1-i] != '?':
                    result = 'Not exist'
                    break
        else:
            result = 'Exist'        
    else:
        for j in range(len(text)//2):
            if text[j] != text[-1-j]:
                result = 'Not exist'
                break
        else:
            result = 'Exist'
    print('#{} {}'.format(test_case, result))