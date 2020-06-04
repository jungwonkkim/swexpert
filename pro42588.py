"""
프로그래머스 42588 탑
https://programmers.co.kr/learn/courses/30/lessons/42588
code jungwonkkim
"""

def solution(heights):
    answer = []
    stack = []
    for i in range(len(heights)):
        while stack:
            if heights[stack[-1]] > heights[i]:
                break
            else:
                stack.pop()
        if stack:
            answer.append(stack[-1]+1)
        else:
            answer.append(0)
        stack.append(i)
    return answer