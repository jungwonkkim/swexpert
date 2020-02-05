#5986. 세 소수

num_list = [True] * 2000
a = int(1000**(1/2))
for i in range(2,a+1):
    if num_list[i] ==True:
        for j in range(i+i, 1000, i):
            num_list[j]  = False
prime_list = [i for i in range(2,1000) if num_list[i] == True]      

      
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    counter = 0
    for i in range(len(prime_list)):
        for j in range(i, len(prime_list)):
            for k in range(j, len(prime_list)):
                if prime_list[i]+prime_list[j]+prime_list[k] == n:
                    counter +=1
                if prime_list[i]+prime_list[j]+prime_list[k] > n :
                    break
    print(f'#{test_case} {counter}')