#1228. [S/W 문제해결 기본] 8일차 - 암호문1

for test_case in range(1, 11):
    n = int(input())
    password = list(map(int, input().split()))
    password = password[:10]
    c = int(input())
    count = 0
    cmd_sline = [[] for _ in range(c)]
    cmd_line = list(input().split())
    for cmd in range(1,len(cmd_line)):
            if cmd_line[cmd] != 'I':
                cmd_line[cmd] = int(cmd_line[cmd])
    for i in range(c):
        count = cmd_line[2]
        cmd_sline[i] = cmd_line[0:3+count]
        del cmd_line[0:3+count]
        
    for j in range(c):
        if cmd_sline[j][1]<10:
            k = cmd_sline[j][1]
            password = password[0:k] + cmd_sline[j][3:] + password[k:]
            password = password[0:10]
    print(f'#{test_case}', end = ' ')
    for pw in password:
        print(pw, end = ' ')
    print()