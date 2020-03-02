#3378. 스타일리쉬 들여쓰기

T = int(input())

for test_case in range(1, T+1):
    p, q = map(int, input().split())
    well_done = [input() for _ in range(p)]
    mine = [input() for _ in range(q)]
    stack = [0,0,0] #소, 중, 대괄호
    for line in well_done:
        cnt = 0
        char_flag:
        for char in line:
            if char =='.' and char_flag == False:
                cnt +=1
                continue
            char_flag = True
            if char =='(':
                stack[0] +=1
                continue
            if char == ')':
                stack[0] -=1
                continue
            if char == '{':
                stack[1] +=1
                continue
            if char == '}':
                stack[1] -=1
            if char == '[':
                stack[2] +=1
            if char ==']':
                stack[2] -=1
            cnt =


