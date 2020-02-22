#프로그래머스 62049 종이접기

def solution(n):
    answer_memo = [[0]]
    if n >=2:
        for i in range(2,n+1):
            new_list = [0,1] * (2**(i-2))
            old_list = answer_memo[-1]
            answer_list = []
            for j in range(2**(i-1)):
                answer_list.append(new_list[j])
                if j != 2**(i-1) -1:
                    answer_list.append(old_list[j])
            answer_memo.append(answer_list)
    answer = answer_memo[-1]
    return answer

N = int(input())
print(solution(N))
