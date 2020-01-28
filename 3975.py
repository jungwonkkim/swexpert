#3975. 승률 비교하기

T = int(input())
result_list = []
for test_case in range(T):
    a, b, c, d = map(int, input().split())
    alice = a/b
    bob = c/d
    if alice>bob:
        result_list.append('ALICE')
    elif alice == bob:
        result_list.append('DRAW')
    else:
        result_list.append('BOB')
for i in range(T):
    print(f'#{i+1} {result_list[i]}')
       