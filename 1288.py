#1288 양을 세는 비뚤어진 방법
T = int(input())
for test_case in range(1, T + 1):
    i = 1
    n = int(input())
    num_set=set()
    num_list=[]
    while (i>0):
        num_list = list(str(n*i))
        for num_str in num_list:
            num_set.add(num_str)
        if len(num_set) ==10:
            print(f'#{test_case} {n*i}') 
            break
        else:
            i=i+1