#백준 17136 색종이붙이기
def check (a,b,size):
    for i in range(a, a+size):
        for j in range(b, b+size):
            if i>9 or j>9:
                return False
            if paper[i][j] == 0 or covered[i][j]:
                return False
    return True


def dfs(r,c,cntarr):
    global min_val
    global covered
    if min_val < 25-sum(cntarr):
        return
    if r == 10 and covered == paper:
        if min_val > 25 - sum(cntarr):
            min_val = 25 - sum(cntarr)
        return
    if r == 10:
        return
    if c == 10:
        dfs(r+1,0,cntarr)
        return
    if paper[r][c] == 0 or covered[r][c]:
        dfs(r,c+1,cntarr)
        return
    for paper_size in range(5,0,-1):
        if cntarr[paper_size-1] == 0 or check(r,c,paper_size) == False:
            continue
        else:
            if paper_size == 1 and cntarr[0] == 0:
                 return
            for cover in range(paper_size, 0,-1):
                if cntarr[cover-1] == 0:
                    continue
                for a in range(r,r+cover):
                    for b in range(c, c+cover):
                        covered[a][b] = 1
                cntarr[cover-1] -=1
                dfs(r, c+cover, cntarr)
                cntarr[cover-1] +=1
                for a in range(r, r+paper_size):
                    for b in range(c, c+paper_size):
                        covered[a][b] = 0
            break


paper = [list(map(int, input().split())) for _ in range(10)]
covered = [[0 for _ in range(10)] for _ in range(10)]
min_val = 26
res = 0
dfs(0, 0, [5, 5, 5, 5, 5])
if min_val  == 26:
    min_val = -1
print(min_val)