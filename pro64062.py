def solution(stones, k):
    answer = 200000001
    length = len(stones)-k
    cnt = 0
    while cnt < length:
        max_val = stones[cnt]
        max_idx = cnt
        for i in range(cnt+1, cnt+k):
            if max_val <= stones[i]:
                max_val = stones[i]
                max_idx = i
        if answer > max_val:
            answer = max_val
        cnt = max_idx+1
    return answer