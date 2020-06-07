"""
프로그래머스 42587 프린터
https://programmers.co.kr/learn/courses/30/lessons/42587
code written by jungwonkkim
"""
def solution(priorities, location):
    priority_counter = {}
    answer = 1
    for priority in priorities:
        if priority in priority_counter:
            priority_counter[priority] += 1
        else:
            priority_counter[priority] = 1
    priorities = [(idx, priorities[idx]) for idx in range(len(priorities))]
    while True:
        i, priority = priorities[0]
        for idx in range(priority+1, 10):
            if idx in priority_counter:
                priorities.append(priorities.pop(0))
                break
        else:
            if i == location:
                break
            else:
                priority_counter[priority] -=1
                if priority_counter[priority] == 0:
                    del priority_counter[priority]
                priorities.pop(0)
                answer += 1
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
