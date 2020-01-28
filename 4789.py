#4789. 성공적인 공연 기획

T = int(input())

for test_case in range(1, T + 1):
    so_list = list(input())
    so_list = [int(so) for so in so_list]
    result = 0
    if len(so_list)==1:
        result = 0
    for i in range(1, len(so_list)):
        if sum(so_list[:i])>=i:
            pass
        else:
            result+= i-sum(so_list[:i])
            so_list[i-1] += i-sum(so_list[:i])
    print(f'#{test_case} {result}')