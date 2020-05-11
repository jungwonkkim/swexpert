"""
swea 5202. 화물도크
code written by jungwonkkim
"""

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    applications = []
    for _ in range(N):
        s, e = map(int, input().split())
        if applications:
            i = len(applications)
            for idx in range(len(applications)):
                if applications[idx][1] < e:
                    continue
                elif applications[idx][1] == e and applications[idx][0] < s:
                    continue
                else:
                    i = idx
                    break
            applications.insert(i, [s,e])
        else:
            applications.append([s, e])
    ans = 1
    end = applications[0][1]
    idx = 1
    while idx < len(applications):
        if applications[idx][0] < end:
            idx +=1
            continue
        else:
            ans +=1
            end = applications[idx][1]
            idx +=1
    print('#{} {}'.format(test_case, ans))

