#1229. [S/W 문제해결 기본] 8일차 - 암호문2

for test_case in range(1, 11):
    n = int(input())
    password = list(map(int, input().split()))
    c = int(input())
    cmd_line = list(input().split())
    for cmd in range(1,len(cmd_line)):
            if cmd_line[cmd] != 'I' and cmd_line[cmd]!='D':
                cmd_line[cmd] = int(cmd_line[cmd])
    for i in range(len(cmd_line)):
        if cmd_line[i] == 'I':
            k = cmd_line[i+2]
            place = cmd_line[i+1]
            password = password[:place] + cmd_line[i+3:i+3+k] + password[place:]
        elif cmd_line[i] =='D':
            place = cmd_line[i+1]
            k = cmd_line[i+2]
            del password[place:place+k]
    print(f'#{test_case}', end = ' ')
    for i in range(10):
        print(password[i], end = ' ')
    print()
            
            
            
       