#1234. [S/W 문제해결 기본] 10일차 - 비밀번호


def pw_making(arr):
    check = -1
    n = len(arr)
    while True:
        for i in range(len(arr)):
            if check == -1:
                check = i
            elif arr[check] == arr[i]:
                arr[check] = 0
                arr[i] = 0
                check = -1
            else:
                check = i
        arr = [num for num in arr if num != 0]
        if n == len(arr):
            return arr
        else:
            n = len(arr)
            check = -1
    


for test_case in range(1, 11):
    a, b = input().split()
    n = int(a)
    password = list(b)
    arr = pw_making(password)
    str = ''.join(arr)
    print(f'#{test_case} {str}')

    
          
            
           
        