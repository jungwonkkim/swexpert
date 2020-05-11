"""
swea 5201 3일차-컨테이너 운반
code written by jungwonkkim
"""

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    loads = list(map(int, input().split()))
    loads.sort(reverse=True)
    trucks = list(map(int, input().split()))
    trucks.sort(reverse=True)
    ans = 0
    l = 0
    for truck in trucks:
        for i in range(l, len(loads)):
            if loads[i] > truck:
                continue
            else:
                ans +=loads[i]
                break
        l = i+1
        if i == len(loads):
            break
    print('#{} {}'.format(test_case, ans))


