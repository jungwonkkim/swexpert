#3314.보충학습과 평균

T = int(input())

for test_case in range(1, T + 1):
    scores = list(map(int, input().split()))
    for i in range(len(scores)):
        if scores[i] <40:
            scores[i] = 40
    print(f'#{test_case} {int(sum(scores)/5)}')
