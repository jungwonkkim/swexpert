#1959번 두 개의 숫자열
T = int(input())

for test_case in range(1, T + 1):
    num_a,num_b = map(int,input().split())
    max_val = 0
    list_a = input().split()
    list_b = input().split()
    list_a = [int(a) for a in list_a]
    list_b = [int(b) for b in list_b]
    if num_b>num_a:
        for i in range(num_b-num_a+1):
            val_count = 0
            for j in range(num_a):
                val_count += (list_a[j] * list_b[j+i])
            if val_count > max_val:
                max_val = val_count
    else:
        for i in range(num_a-num_b+1):
            val_count = 0
            for j in range(num_b):
                val_count += (list_a[j+i] * list_b[j])
            if val_count > max_val:
                max_val = val_count
    print(f'#{test_case} {max_val}')