#4047. 영준이의 카드 카운팅

T = int(input())

for test_case in range(1, T + 1):
    S_count = ['01','02','03','04','05','06','07','08','09','10','11','12','13']
    D_count = ['01','02','03','04','05','06','07','08','09','10','11','12','13']
    H_count = ['01','02','03','04','05','06','07','08','09','10','11','12','13']
    C_count = ['01','02','03','04','05','06','07','08','09','10','11','12','13']
    card_deck = input()
    result = 0
    for i in range(len(card_deck)):
        if card_deck[i] =='S':
            if card_deck[i+1:i+3] in S_count:
                S_count.remove(card_deck[i+1:i+3])
            else:
                result = -1
        elif card_deck[i] =='D':
            if card_deck[i+1:i+3] in D_count:
                D_count.remove(card_deck[i+1:i+3])
            else:
                result = -1         
        elif card_deck[i] =='H':
            if card_deck[i+1:i+3] in H_count:
                H_count.remove(card_deck[i+1:i+3])
            else:
                result = -1        
        elif card_deck[i] =='C':
            if card_deck[i+1:i+3] in C_count:
                C_count.remove(card_deck[i+1:i+3])
            else:
                result = -1    
    s_counter = len(S_count)
    d_counter = len(D_count)
    h_counter = len(H_count)
    c_counter = len(C_count)
    if result == -1:
        print(f'#{test_case} ERROR')
    else:
        print(f'#{test_case} {s_counter} {d_counter} {h_counter} {c_counter}')
    