#1824. 혁진이의 프로그램 검증
nextpoint = {'<':(0,-1), '>':(0,1), '^':(-1,0),  'v':(1,0)}
def nextSearch(x,y,dirt):
    return( (x + nextpoint[dirt][0]) % R, (y + nextpoint[dirt][1]) % C)

def execution(fa, fb, fval, fdirt):
    path = [[list() for _ in range(C)] for _ in range(R)]
    stack= [(fa,fb, fval, fdirt)]
    while stack:
        a, b, val, dirt = stack.pop()
        if path[a][b] and (val, dirt) in path[a][b]:
            continue
        path[a][b].append((val, dirt))
        if command[a][b] == '@':
            return True
        if command[a][b] == '<':
            newa, newb = nextSearch(a, b,'<')
            stack.append((newa, newb, val, '<'))
            continue
        if command[a][b] == '>':
            newa, newb = nextSearch(a, b, '>')
            stack.append((newa,newb,val,'>'))
            continue
        if command[a][b] == '^':
            newa, newb = nextSearch(a, b, '^')
            stack.append((newa, newb, val, '^'))
            continue
        if command[a][b] =='v':
            newa, newb = nextSearch(a, b, 'v')
            stack.append((newa,newb,val,'v'))
            continue
        if command[a][b] == '_':
            if val == 0:
                newa, newb = nextSearch(a, b, '>')
                stack.append((newa, newb, val, '>'))
                continue
            else:
                newa, newb = nextSearch(a, b, '<')
                stack.append((newa, newb, val, '<'))
                continue
        if command[a][b] == '|':
            if val == 0:
                newa, newb = nextSearch(a, b, 'v')
                stack.append((newa, newb, val, 'v'))
                continue
            else:
                newa, newb = nextSearch(a, b, '^')
                stack.append((newa, newb, val, '^'))
                continue
        if command[a][b] == '.':
            newa, newb = nextSearch(a, b, dirt)
            stack.append((newa, newb, val, dirt))
            continue
        if command[a][b] == '+':
            new_val = (val+1)%16
            newa, newb = nextSearch(a, b, dirt)
            stack.append((newa, newb, new_val, dirt))
            continue
        if command[a][b] == '-':
            new_val = (val-1)%16
            newa, newb = nextSearch(a, b, dirt)
            stack.append((newa, newb, new_val, dirt))
            continue
        if command[a][b] == '?':
            newa, newb = nextSearch(a, b, '<')
            stack.append((newa, newb, val, '<'))
            newa, newb = nextSearch(a, b, '>')
            stack.append((newa, newb, val, '>'))
            newa, newb = nextSearch(a, b, '^')
            stack.append((newa, newb, val, '^'))
            newa, newb = nextSearch(a, b, 'v')
            stack.append((newa, newb, val, 'v'))
            continue
        else:
            new_val = int(command[a][b])
            newa, newb = nextSearch(a, b, dirt)
            stack.append((newa, newb, new_val, dirt))
    return False

T = int(input())

for test_case in range(1, T+1):
    R, C = map(int, input().split())
    command = [list(input()) for _ in range(R)]
    if execution(0,0,0,'>'):
        res = 'YES'
    else:
        res = 'NO'
    print('#{} {}'.format(test_case, res))




