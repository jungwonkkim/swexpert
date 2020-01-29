#3282. 0/1 Knapsack

def knapsack(K , w_list , c_list , N): 
    if N == 0 or K == 0 : 
        return 0
    if (w_list[N-1] > K): 
        return knapsack(K , w_list , c_list , N-1)
    else: 
        return max(c_list[N-1] + knapsack(K-w_list[N-1], w_list , c_list , N-1), 
                   knapsack(K , w_list , c_list , N-1)) 

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    w_list = []
    c_list = []
    for i in range(N):
        w, c= map(int,input().split())
        w_list.append(w)
        c_list.append(c)
    print(f'#{test_case} {knapsack(K, w_list, c_list, N)}')

    

    