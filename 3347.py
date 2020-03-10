#3347.올림픽 종목 투표

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    voted = [False for _ in range(M)]
    max_vote = 0
    ans = -1
    for i in range(N):
        cnt = 0
        for j in range(M):
            if voted[j] == False and A[i] <= B[j]:
                cnt +=1
                voted[j] = True
        if max_vote < cnt:
            max_vote = cnt
            ans = i +1
    print('#{} {}'.format(test_case, ans))