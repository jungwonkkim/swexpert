#code created by jungwonkkim

#1204 :  최빈수 구하기

def solve(arr):
    max_val_count = 0
    max_val = 0
    for i in range(100,-1,-1):
        count = arr.count(i)
        if count>max_val_count:
            max_val_count = count
            max_val = i
    return max_val
            

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a= int(input())
    str_list = input().split()
    num_list = [int(num) for num in str_list]
    b = solve(num_list)
    print(f'#{a} {b}')
	