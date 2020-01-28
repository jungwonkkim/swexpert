#5431. 민석이의 과제 체크하기

T = int(input())

for test_case in range(1, T + 1):
    stu, smt = map(int, input().split())
    submitted = set(list(map(int, input().split())))
    student = set([i+1 for i  in range(stu)])
    not_yet = list(student - submitted)
    print(f'#{test_case}', end = ' ')
    for i in not_yet:
        print(i, end = ' ')
    print()
        
    
