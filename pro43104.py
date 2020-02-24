#프로그래머스 43104 타일장식물

def solution(N):
    fibo = [1,1]
    if N >2:
        for i in range(2, N+1):
            fibo.append(fibo[i-1] + fibo[i-2])
    answer = 2*(fibo[N]+fibo[N-1])
    return answer