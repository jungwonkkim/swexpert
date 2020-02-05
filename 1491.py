#1491.원재의 벽 꾸미기

T = int(input())

for test_case in range(1, T + 1):
    number, A, B = map(int, input().split())
    values = []
    min_num = (int(number**(1/2)) **2)
    for N in range(min_num, number+1):
        for R in range(int(N**(1/2)),0, -1):
            if N % R ==0:
                C = N//R
                value = A * abs(R-C) + B * (number -N)
                values.append(value)
    print('#{} {}'.format(test_case, min(values)))