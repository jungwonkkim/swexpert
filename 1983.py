grading = {0:'A+', 1:'A0', 2:'A-', 3:'B+', 4:'B0', 5:'B-', 6: 'C+', 7:'C0', 8: 'C-', 9:'D0'}

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    total_list = []
    for i in range(n):
        score_list= list(map (int, input().split()))
        total_score = score_list[0]*0.35 + score_list[1] * 0.45 + score_list[2]*0.25
        total_list.append(total_score)
    student = total_list[k-1]
    total_list.sort()
    total_list.reverse()
    rank = total_list.index(student)
    print(rank)