#1234. [S/W 문제해결 기본] 10일차 - 비밀번호

for test_case in range(1, T+1):
    num , pw = input().split()
    num = int(num)


   for i in range(len(pw)):
        if pw[i] == pw[i+1]:
            pw[i:i+2] = '**'
        pw = pw.replace('**','',5)
    print(pw)
                   
                  