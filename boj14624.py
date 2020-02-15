cmd = int(input())
if cmd%2:
    string = '*' * cmd + '\n'
    string +=' '*(cmd//2) + '*' + '\n'
    for i in range(1, cmd//2+1):
        string += ' ' * (cmd//2-i) + '*' + ' '*(2*i-1) + '*' + '\n'

    print(string)
else:
    print('I LOVE CBNU')