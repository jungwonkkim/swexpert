T = int(input())
for tc in range(1,T+1):
    K,N,M = map(int,input().split()) #언니 일단 얘네들을 왼쪽에 변수 세개 주고... 굳이..list로 받지 않아도 될 것 같아요
    bs = list(map(int,input().split()))
    bs1 = [0]*(N+1)
    for i in bs:
        bs1[i] = 1
    if K < bs1[0]:
        ans = 0
    cur = 0
    cnt = 0
    while cur<N:
        for k in range(K,0,-1):
            if cur+k >=N:
                cur = cur+k
                break
            elif bs1[cur+k] == 1:
                cnt+=1
                cur = cur + k
                break
        else:
            cnt = 0
            break

    print('#{} {}'.format(tc,cnt))