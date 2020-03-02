#3752. 가능한 시험 점수

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    score_list = list(map(int, input().split()))
    total = {0}
    for i in score_list:
        new = set()
        for t in total:
            new.add(t+i)
        total = total | new
    print('#{} {}'.format(test_case, len(total)))