#6190. 정곤이의 단조 증가하는 수

def sim_inc(n):
    re = n%10
    n = int((n-re)/10)
    while n!=0:
        if n%10>re:
            return False
        re = n%10
        n = int((n-re)/10)
    return True
 
T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    num_list = list(map(int,input().split()))
    result = -1
    for i in range(n):
        for j in range(i):
            if result<num_list[i]*num_list[j]:
                if sim_inc(num_list[i]*num_list[j]):
                    result = num_list[i]*num_list[j]
    print(f'#{test_case} {result}')