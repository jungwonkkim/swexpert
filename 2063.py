a=int(input())
half = int(round((a-1)/2,0))
b = input().split()
num_list = [int(num) for num in b]
num_list.sort()
print(num_list[half])