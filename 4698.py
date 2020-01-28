#4698. 테네스의 특별한 소수

T = int(input())

num_list = [True] * 1000000
for i in range(2,1001):
    if num_list[i] ==True:
        for j in range(i+i, 1000000, i):
            num_list[j]  = False
prime_list = [i for i in range(2,1000000) if num_list[i] == True]            

for test_case in range(1, T + 1):
    d, a, b = map(int, input().split())
    d = str(d)
    ab_list = [str(prime) for prime in prime_list if prime>=a and prime<=b]
    ab_list = [prime for prime in ab_list if d in prime]
    print(f'#{test_case} {len(ab_list)}')
        
    