#4837. 부분집합의 합

#집합의 원소 개수가 작기 때문에 부분집합을 다 만들어 놓는 방향으로 했는데, 만약 12가 아닌 큰 수 였으면 DFS를 이용해서 부분집합을 만들어야 할 것 같아요. 

arr=[i+1 for i in range(12)]  #부분집합의 경우의 수를 다 만들어 놓으면 큰 수의 테스트케이스에 유리할 것 같아 먼저 부분집합을 만들어 놓았다.
subset_array = []
n=len(arr)
for i in range(1<<n): #부분집합의 모든 경우의 수(어제 배운 비트연산 이용)
    subset_list = []
    for j in range(n):
        if i & (1<<j):
            subset_list.append(arr[j])
    subset_array.append(subset_list)

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split()) #테스트 케이스 별로 부분집합 원소의 수 N과 부분집합의 합 K를 만족하는 테스트 케이스를 구한다
    counter = 0
    for arr in subset_array:
        if len(arr)==N and sum(arr) == K:
            counter +=1 #위의 경우 만족 시켰을 경우 플러스 1해주기
    print(f'#{test_case} {counter}')
