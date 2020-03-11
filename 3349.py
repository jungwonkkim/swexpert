#3349. 최솟값으로 이동하기


T = int(input())
for test_case in range(1, T+1):
    W, H, N = map(int, input().split())
    a1, b1 = map(int, input().split())
    cnt = 0
    for i in range(1, N):
        a2, b2 = map(int, input().split())
        if a2>a1 and b2>b1:
            cnt += max(a2-a1, b2-b1)
            continue
        if a2<a1 and b2<b1:
            cnt += max(a1-a2, b1-b2)
            continue
        cnt += abs(a2-a1) + abs(b2-b1)
    print('#{} {}'.format(test_case, cnt))

# 3349. 최솟값으로 이동하기 리스트 없이 for 한번만
T = int(input())
for test_case in range(1, T + 1):
    W, H, N = map(int, input().split())
    a, b = map(int, input().split())
    cnt = 0
    for i in range(1, N):
        a1, b1 = a, b
        a, b = map(int, input().split())
        if a > a1 and b > b1:
            cnt += max(a - a1, b - b1)
            continue
        if a < a1 and b < b1:
            cnt += max(a1 - a, b1 - b)
            continue
        cnt += abs(a - a1) + abs(b - b1)
    print('#{} {}'.format(test_case, cnt))