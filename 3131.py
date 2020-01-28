#3131. 100만 이하의 모든 소수

num_list = [True] * 1000000
for i in range(2,1001):
    if num_list[i] ==True:
        for j in range(i+i, 1000000, i):
            num_list[j]  = False
prime_list = [i for i in range(2,1000000) if num_list[i] == True]            
for prime in prime_list:
    print(prime, end = ' ')