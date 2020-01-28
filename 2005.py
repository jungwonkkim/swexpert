#2005 파스칼

def Pascal(n):
    line_list = [0] * n
    if n == 1:
        line_list = [1]
    if n ==2:
        line_list = [1,1]
    else:
        for i in range(n):
            if i ==0:
                line_list[i] = 1
            elif i ==n-1:
                line_list[i] = 1
            else:
                line_list[i] =sum(Pascal(n-1)[i-1:i+1])
    return line_list
           

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')
    n = int(input())
    for i in range(1,n+1):
        for j in range(i):
            print(Pascal(i)[j], end = ' ')
        print()    
        