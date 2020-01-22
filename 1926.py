#1926 369

n = int(input())
num_list =[]
for i in range(1, n+1):
    num_list.append(i)
num_list = [str(num) for num in num_list]
for char in num_list:
    count = 0
    count = char.count('3') + char.count('6') + char.count('9')
    if count ==1:
        print('-', end = ' ')
    elif count ==2:
        print('--', end = ' ')
    elif count ==3:
        print('---', end = ' ')
    else:
        print(char, end = ' ')