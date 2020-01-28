#2805. 농작물 수확하기
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    result = 0
    farm = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        farm[i] = list(map(int, input()))
    half = int((n-1)/2)
    for i in range(half):
        result += sum(farm[i][half-i: half+i+1])
    result +=sum(farm[half])
    for i in range(half+1, n):
        result += sum(farm[i][i-half:n-i+half])
    print(f'#{test_case} {result}')
        
        
    
        