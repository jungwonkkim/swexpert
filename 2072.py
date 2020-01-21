

T = int(input())

for test_case in range(1, T + 1):
    h= input().split()
    sum =0
    for num in h:
        if int(num)%2==1:
            sum+=int(num)
    print(f'#{test_case} {sum}')