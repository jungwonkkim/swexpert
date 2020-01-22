#1970 거스름돈!!!

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    money = int(input())
    c_oman = 0
    c_man = 0
    c_ochun =0
    c_chun = 0
    c_obaek = 0
    c_baek =0
    c_osip = 0
    c_sip = 0
    while money>=50000:
        money -=50000
        c_oman+=1
    while money>=10000:
        money -=10000
        c_man +=1
    while money>=5000:
        money -=5000
        c_ochun+=1
    while money >=1000:
        money -=1000
        c_chun +=1
    while money>= 500:
        money -=500
        c_obaek +=1
    while money >=100:
        money -=100
        c_baek+=1
    while money >=50:
        money -=50
        c_osip +=1
    while money >=10:
        money -=10
        c_sip +=1
    print(f'#{test_case}')
    print(f'{c_oman} {c_man} {c_ochun} {c_chun} {c_obaek} {c_baek} {c_osip} {c_sip}')
    
          
        
        