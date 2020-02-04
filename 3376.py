#3376. 파도반 수열

def padoban(n):
    global p_list
    p_list = [1,1,1,2,2]
    if n <= 5:
        return p_list[n-1]
    if n>5:
        for i in range(5, n):
            p = p_list[i-1] + p_list[i-5]
            p_list.append(p)
        return p_list[n-1]
   

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    result = padoban(n)
    print(f'#{test_case} {result}')
