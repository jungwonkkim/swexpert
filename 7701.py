# 7701. 염라대왕의 이름 정렬

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    sorter = [[] for _ in range(50)]
    for i in range(num):
        text = input()
        sorter[len(text)].append(text)
    print('#{}'.format(test_case))
    for a in range(50):
        if sorter[a]:
            sorter[a].sort()
            sorter[a] = list(set(sorter[a]))
            for ans in sorter[a]:
                print(ans)


