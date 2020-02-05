#4615. 재미있는 오셀로


delta = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    o_board = [[0 for _ in range(n)] for _ in range(n)]
    half = int(n/2)
    o_board[half-1][half-1] = o_board[half][half] = 2
    o_board[half][half-1] = o_board[half-1][half] = 1
    
    for i in range(m):
        c, r, s = map(int, input().split())
        r-=1
        c-=1
        o_board[r][c] = s
        for i in range(8):
            one_flag = False
            flag_list = []
            dx = delta[i][0]
            dy = delta[i][1]
            x = r
            y = c
            while x+dx>-1 and x+dx<n and y+dy>-1 and y+dy<n :
                x += dx
                y += dy
                if o_board[x][y] == 0:
                    break
                elif o_board[x][y] == s:
                    one_flag =  True
                    break
                else:
                    flag_list.append((x,y))
            if one_flag == True:
                for switch in flag_list:
                    o_board[switch[0]][switch[1]] = s      
    one_counter = 0
    two_counter = 0
    for a in range(n):
        for b in range(n):
            if o_board[a][b] ==1:
                one_counter +=1
            if o_board[a][b] ==2:
                two_counter +=1
    print('#{} {} {}'.format(test_case, one_counter, two_counter))
            
        