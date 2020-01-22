#1976번 시간 분!

T = int(input())

for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int,input().split())
    minute = m1+m2
    if minute>=60:
        minute = minute - 60
        h1+=1
    hour = h1+h2     
    if hour>12:
        hour = hour-12
    print(f'#{test_case} {hour} {minute}')