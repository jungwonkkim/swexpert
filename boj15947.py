#아기 석환 뚜루루 뚜루

lyric = ['baby','sukhwan','tururu','turu','very','cute','tururu','turu','in','bed','tururu','turu','baby','sukhwan']
n = int(input())
line = (n-1) % 14
if line == 2 or line == 6 or line == 10:
    recur = n//14
    if recur >= 3:
        print('tu+ru*{}'.format(recur+2))
    else:
        ans = 'tururu'+ 'ru'*recur
        print(ans)
elif line ==3 or line == 7 or line == 11:
    recur = n//14
    if recur >=4:
        print('tu+ru*{}'.format(recur+1))
    else:
        ans = 'turu' + 'ru'*recur
        print(ans)
else:
    print(lyric[line])