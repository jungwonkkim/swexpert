#백준 2502. 떡먹는 호랑이

def factorial(n):
    factoa = [1,0]
    factob = [0,1]
    for i in range(2, n):
        factoa.append(factoa[-1] + factoa[-2])
        factob.append(factob[-1] + factob[-2])
    return (factoa[n-1], factob[n-1])


D, K = map(int,input().split())
x,y = factorial(D)
a = 1
while True :
    if (K-(a*x)) % y == 0:
        b = int((K-(a*x))/y)
        break
    a += 1
print(a)
print(b)

