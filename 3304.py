#3304. 최장 공통 부분 수열

T = int(input())
for test_case in range(1, T+1):
    stringA, stringB = input().split()
    row = len(stringA)
    column = len(stringB)
    subsequence = [[0 for _ in range(row+1)] for _ in range(column+1)]
    for i in range(0,column):
        for j in range(0, row):
            if stringB[i] == stringA[j]:
                subsequence[i+1][j+1] = subsequence[i][j] +1
            else:
                subsequence[i+1][j+1] = max(subsequence[i+1][j], subsequence[i][j+1])
    print('#{} {}'.(test_case, subsequence[column][row]))