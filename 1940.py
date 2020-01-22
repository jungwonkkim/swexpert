#1940 가라 RC카!

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    dist = 0
    speed = 0
    for command in range(1, n+1):
        str= input()
        if len(str)==1:
            dist+= speed
        else:
            c,s =map(int,str.split())
            if c==1:
                speed+=s
                dist+=speed
            else:
                speed-=s
                if speed<0:
                    speed=0
                dist+=speed
    print(f'#{test_case} {dist}')