#4261. 빠른 휴대전화 키패드
def word_to_num(string):
    num = ''
    for s in string:
        if s=='a' or s=='b' or s=='c':
            num += '2'
            continue
        if s =='d' or s=='e' or s=='f':
            num+='3'
            continue
        if s=='g' or s=='h' or s=='i':
            num += '4'
            continue
        if s=='j' or s=='k' or s=='l':
            num +='5'
            continue
        if s =='m' or s=='n' or s=='o':
            num +='6'
            continue
        if s=='p' or s=='q' or s=='r' or s=='s':
            num +='7'
            continue
        if s== 't' or s=='u' or s=='v':
            num +='8'
            continue
        if s=='w' or s=='x' or s=='y' or s== 'z':
            num+='9'
            continue
    return num


T = int(input())

for test_case in range(1, T+1):
    S, N = input().split()
    word_list = list(input().split())
    cnt = 0
    for word in word_list:
        if word_to_num(word) == S:
            cnt+=1
    print('#{} {}'.format(test_case, cnt))
