#백준 10996.별찍기 21

n = int(input())
str1 = '* ' * (n - (n // 2))
str2 = ''
if n>=2:
    str2 = ' *' * (n // 2)
for i in range(n):
    print(str1[:-1])
    if str2:
        print(str2)
