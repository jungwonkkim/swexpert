#2806. N-Queen

def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True
        
        
#한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result
    
    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    row = [0]*N
    result = 0
    dfs(0)
    print(f'#{test_case} {result}')
