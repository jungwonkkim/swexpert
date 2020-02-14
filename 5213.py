#5213.진수의 홀수 약수

result = []

T = int(input())
for test_case in range(1, T+1):
    L, R = map(int, input().split())
    for num in range(L,R+1):
        while num%2 == 0:
            num = int(num/2)
