#3809.py


def find(string):
    num = 0
    while True:
        if str(num) in string:
            num +=1
        else:
            return num


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    my_str = ''
    while len(my_str) != n:
        my_str += ''.join(input().split())
    result = find(my_str)
    
    print(f'#{test_case} {result}')