#4013. [모의 SW 역량테스트] 특이한 자석
magnets = [list(map(int,input())) for _ in range(4)]
K = int(input())
cnt = 0
while cnt < K:
    m, c = map(int, input().split())
    move = [0 for _ in range(4)]
    move[m-1] = c
    n = 1
    while m+n<5:
        if c == 1:
            c = -1
        else:
            c = 1
        if magnets[m+n-2][2] != magnets[m+n-1][6]:
            move[m+n-1] = c
        else:
            break
        n +=1
    n = 1
    c = move[m-1]
    while m-n >= 1 :
        if c == 1:
            c = -1
        else:
            c = 1
        if magnets[m-n][6] != magnets[m-n-1][2]:
            move[m-n-1] = c
        else:
            break
        n+=1
    for i in range(4):
        if move[i] == 1:
            temp = magnets[i][7]
            for j in range(7, 0, -1):
                magnets[i][j] = magnets[i][j-1]
            magnets[i][0] = temp
        if move[i] == -1:
            temp = magnets[i][0]
            for j in range(7):
                magnets[i][j] = magnets[i][j+1]
            magnets[i][7] = temp
    cnt +=1

total = 0
for i in range(4):
    if magnets[i][0]:
        total += 2**i
print(total)