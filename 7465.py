
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    village = [[0 for _ in range(N)] for _ in range(N)]
    visited = [False for _ in range(N)]
    muri = 0
    if M:
        for i in range(M):
            a, b = map(int, input().split())
            village[a-1][b-1] = village[b-1][a-1] = 1
    for c in range(N):
        stack = []
        for d in range(N):
            if village[c][d]:
                visited[c] = True
                stack.append(d)
                village[c][d] = village[d][c] = 0
        if stack:
            muri +=1
        while stack:
            search = stack.pop()
            visited[search] = True
            for person in range(N):
                if village[search][person] and visited[person] == False:
                    village[search][person] = village[person][search] = 0
                    stack.append(person)
    for v in visited:
        if v == False:
            muri += 1

    print('#{} {}'.format(test_case, muri))