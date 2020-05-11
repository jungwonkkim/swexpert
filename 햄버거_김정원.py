#5215. 햄버거 다이어트

def knapSack(W , wt , val , n): 
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), knapSack(W , wt , val , n-1)) 

T= int(input())
for test_case in range(1, T + 1):
    v_list = []
    c_list = []
    N, W = map(int, input().split())
    for i in range(N):
        c, v = map(int, input().split())
        v_list.append(v)
        c_list.append(c)
    value = knapSack(W,v_list, c_list, N)
    print(f'#{test_case} {value}')
    
