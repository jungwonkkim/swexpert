# #3282. 0/1 Knapsack
#
# def knapsack(K , w_list , c_list , N):
#     if N == 0 or K == 0 :
#         return 0
#     if (w_list[N-1] > K):
#         return knapsack(K , w_list , c_list , N-1)
#     else:
#         return max(c_list[N-1] + knapsack(K-w_list[N-1], w_list , c_list , N-1),
#                    knapsack(K , w_list , c_list , N-1))
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N, K = map(int, input().split())
#     w_list = []
#     c_list = []
#     for i in range(N):
#         w, c= map(int,input().split())
#         w_list.append(w)
#         c_list.append(c)
#     print(f'#{test_case} {knapsack(K, w_list, c_list, N)}')

#
# # 3282. 0/1 Knapsack
# def knapsack(pos, capacity):
#     if pos == N:
#         return 0
#     ret = dp[pos][capacity]
#     if ret != -1:
#         return ret
#     if item[pos][0] <= capacity:
#         ret = knapsack(pos + 1, capacity - item[pos][0]) + item[pos][1]
#     ret = max(ret, knapsack(pos + 1, capacity))
#     dp[pos][capacity] = ret
#     return
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N, K = map(int, input().split())
#     item = [[0 for _ in range(2)] for _ in range(N)]
#     for i in range(N):
#         v, c = map(int, input().split())
#         item[i][0] = v
#         item[i][1] = c
#     dp = [[-1 for _ in range(1000)] for _ in range(N)]
#     result = knapsack(0, K)
#     print('#{} {}'.format(test_case, result))


    # 3282.Knapsack
    def knapsack(W, wt, val, n):  # W: 배낭의 무게한도, wt: 각 보석의 무게, val: 각 보석의 가격, n: 보석의 수
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]  # DP를 위한 2차원 리스트 초기화
        for i in range(n + 1):
            for w in range(W + 1):  # 각 칸을 돌면서
                if i == 0 or w == 0:  # 0번째 행/열은 0으로 세팅
                    K[i][w] = 0
                elif wt[i - 1] <= w:  # 점화식을 그대로 프로그램으로
                    K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])  # max 함수 사용하여 큰 것 선택
                else:
                    K[i][w] = K[i - 1][w]
        return K[n][W]


    T = int(input())

    for test_case in range(1, T + 1):
        wt = []
        val = []
        N, K = map(int, input().split())
        for i in range(N):
            w, v = map(int, input().split())
            wt.append(w)
            val.append(v)
        print('#{} {}'.format(test_case, (knapsack(K, wt, val, N))))