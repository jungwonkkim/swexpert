#5550. 나는 개구리로소이다

T = int(input())
for test_case in range(1, T+1):
    frogs = input()
    frog = [0,0,0,0,0]
    waiting = 0
    result = 0
    for f in frogs:
        if f == 'c':
            if waiting:
                waiting -=1
                frog[0] +=1
            else:
                frog[0]+=1
        elif f == 'r':
            if frog[0]> frog[1]:
                frog[1] +=1
            else:
                result = -1
                break
        elif f =='o':
            if frog[1]> frog[2]:
                frog[2] +=1
            else:
                result = -1
                break
        elif f =='a':
            if frog[2]>frog[3]:
                frog[3] +=1
            else:
                result = -1
                break
        else:
            if frog[3]>frog[4]:
                frog[0] -=1
                frog[1] -=1
                frog[2] -=1
                frog[3] -=1
                waiting +=1
            else:
                result = -1
                break
    if frog[0]:
        result = -1
    elif result != -1:
        result = waiting

    print('#{} {}'.format(test_case, result))