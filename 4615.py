T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    o_board = [[0 for _ in range(n)] for _ in range(n)]
    half = int(n/2)
    o_board[half-1][half-1] = 2
    o_board[half][half] =2
    o_board[half][half-1] = 1
    o_board[half-1][half]=1
    for i in range(m):
        r, c, s = map(int, input().split())
        r-=1
        c-=1
        o_board[r][c] = s
        if c<n-2 and o_board[r][c+1]:
            for i in range(c+1, n):
                if o_board[r][i] == s:
                    for j in range(c, i):
                        o_board[r][j] = s
                    break
        if c>1 and o_board[r][c-1]:
            for i in range(c-1, -1, -1):
                if o_board[r][i] ==s:
                    for j in range(i, c):
                        o_board[r][j] =s
                    break
        if r<n-2 and o_board[r+1][c]:
            for i in range(r+1, n):
                if o_board[i][c] ==s:
                    for j in range(r,i):
                        o_board[j][c] =s
                    break
        if r>1 and o_board[r-1][c]:
            for i in range(r-1, -1, -1):
                if o_board[i][c] ==s:
                    for j in range(i,r):
                        o_board[j][c] =s
                    break
        if r>1 and c>1 and o_board[r-1][c-1]:
            diff = r - c
            for i in range(c-1, -1, -1):
                if i+diff > -1 and i+diff < n :
                    if o_board[i+diff][i] == s:
                        for j in range(i , c):
                            o_board[j+diff][j] = s
                        break
        if r>1 and c<n-2 and o_board[r-1][c+1] :
            diff = r+c
            for i in range(r-1, -1, -1):
                if diff-i>-1:
                    if o_board[i][diff-i] == s:
                        for j in range(i , r):
                            o_board[j][diff-j] = s
                        break
        if r < n-2 and c < n-2 and o_board[r+1][c+1] :
            diff = r - c
            for i in range(c+1, n):
                if i+diff > -1 and i+diff < n :
                    if o_board[i+diff][i] == s:
                        for j in range(c, i):
                            o_board[j+diff][j] = s
                        break
        if r< n-2 and c>1 and o_board[r+1][c-1]:
            diff = r+c
            for i in range(r+1, n):
                if diff-i> -1:
                    if o_board[i][diff-i] == s:
                        for j in range(i , r):
                            o_board[j][n-j] = s
                        break
                    
    one_count = 0
    two_count = 0
    for i in range(n):
        for j in range(n):
            if o_board[i][j] ==1:
                one_count +=1
            if o_board[i][j] ==2:
                two_count +=1
    print(f'#{test_case} {one_count} {two_count}')
                        
                
                
                        
                
                
                        
                
                