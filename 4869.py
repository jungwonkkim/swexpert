def papermaking(paper_com, paper_length):
    if paper_length ==N and paper_com not in result_list:
        result_list.append(paper_com)
    if paper_length <N:
        for paper in paper_type.keys():
            if paper_type[paper]<N-paper_length:
                paper_com += paper
                paper_length +=paper_type[paper]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    paper_type = {'a':2,'b':2,'c':1}
    result_list = []
    N = int(input())//10
    for paper in paper_type.keys():
        paper_com = ''
        paper_length = 0
        papermaking(paper_com, paper_length)
    print('#{} {}'.format(test_case, len(result_list)))
    