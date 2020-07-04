"""
백준 1144 싼비용
https://www.acmicpc.net/problem/1144
code written by jungwonkkim
"""

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[float('inf') for _ in range(M)] for _ in range(N)]
for n in range(N):
    for m in range(M):
        if m == 0:
            if n == 0:
                dp[n][m] = arr[n][m]
            else:
                dp[n][m] = min(arr[n][m], dp[n-1][m] + arr[n][m])
        elif n == 0:
            dp[n][m] = min(arr[n][m], dp[n][m-1] + arr[n][m])
        else:
            dp[n][m] = min(arr[n][m], dp[n][m-1] + arr[n][m], dp[n-1][m] + arr[n][m])
answer = 0
for n in range(N):
    for m in range(M):
        if dp[n][m] < answer:
            answer = dp[n][m]

print(answer)