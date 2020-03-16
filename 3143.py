#3143. 가장 빠른 문자열 타이핑

T = int(input())
for test_case in range(1, T+1):
    A, B = input().split()
    cnt = 0
    char = 0
    while char< len(A):
        if A[char:char+len(B)] == B:
            cnt +=1
            char = char+len(B)
        else:
            cnt +=1
            char+=1
    print('#{} {}'.format(test_case, cnt))