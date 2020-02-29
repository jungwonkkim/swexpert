#5658. [모의 SW 역량테스트] 보물상자 비밀번호

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    s = N//4
    numbers = input()
    candidates = set()
    a = 0
    while a<s:
        candidates.add(int('0x'+numbers[:s],16))
        candidates.add(int('0x'+numbers[s:2*s],16))
        candidates.add(int('0x'+numbers[2*s:3*s],16))
        candidates.add(int('0x'+numbers[3*s:],16))
        numbers = numbers[-1]+numbers[:-1]
        a+=1
    candidates = list(candidates)
    candidates.sort()
    candidates.reverse()
    print('#{} {}'.format(test_case, candidates[K-1]))