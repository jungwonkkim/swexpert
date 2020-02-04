#2750 수 정렬하기

n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
num_list.sort()
for i in range(n):
    print(num_list[i])
