
def solution(stones, k):
    answer = 200000001
    cnt = 0
    while cnt < len(stones)-k:
        max_val = 0
        max_idx = -1
        for i in range(cnt, cnt+k):
            if max_val < stones[i]:
                max_val = stones[i]
                max_idx = i
        if answer > max_val:
            answer = max_val
        cnt = max_idx+1
    return answer

arr= [2,4,5,3,2,1,4,2,5,1]
num = 3

print(solution(arr, num))
