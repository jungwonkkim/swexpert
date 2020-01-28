#4466. 최대 성적표 만들기

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort()
    scores.reverse()
    result = 0
    result = sum(scores[0:k])
    print(f'#{test_case} {result}')
