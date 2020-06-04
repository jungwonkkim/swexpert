"""
5521 상원이의 생일파티
jungwonkkim
"""

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    friends = [[0 for _ in range(N)] for _ in range(N)]
    visited = [False for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1][b-1] = friends[b-1][a-1] = 1
    queue = [0]
    cnt = 0
    invitation = 0
    while cnt < 2:
        new_queue = []
        for q in queue:
            for i in range(1, N):
                if visited[i] == False and friends[q][i]:
                    visited[i] = True
                    invitation += 1
                    new_queue.append(i)
        queue = [el for el in new_queue]
        cnt +=1
    print('#{} {}'.format(test_case, invitation))
