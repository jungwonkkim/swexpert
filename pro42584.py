"""
프로그래머스 42584 주식가격
https://programmers.co.kr/learn/courses/30/lessons/42584
code written by jungwonkkim
"""
def solution(prices):
    answer = []
    queue = [-1] * len(prices)
    time = 0
    while prices:
        price = prices.pop(0)
        while stack:
            if stack[-1] > price:
                stack.pop()

            else:
                break
        stack.append(price)
        time += 1

