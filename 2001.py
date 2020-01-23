#2001 파리

T = int(input())

for test_case in range(1, T + 1):
    max_val = 0
    sum = 0
    n, k = map(int, input().split())
    pari_mari = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        pari_list = list(map(int, input().split()))
        for j in range(n):
            pari_mari[i][j] = pari_list[j]
    for i in range(n-k+1):
        for j in range(n-k+1):
            sum = 0
            for l in range(i, i+k):
                for m in range(j, j+k):
                    sum += pari_mari[l][m]
                if sum >max_val :
                    max_val = sum
                
    print(f'#{test_case} {max_val}')        