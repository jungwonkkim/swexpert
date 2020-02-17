#백준2839. 설탕배달

N = int(input())
a = 0
b = 0
while True:
    if (N - (3 * a)) % 5 == 0:
        b = (N-(3*a))//5
        break
    if (N-(3*a)) ==0:
        break
    if (N-(3*a)) <0:
        a = 0
        b = -1
        break
    a += 1
print(a+b)