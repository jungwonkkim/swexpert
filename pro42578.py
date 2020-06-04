"""
프로그래머스 42578 위장
https://programmers.co.kr/learn/courses/30/lessons/42578
code written by jungwonkkim
"""

def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1
    cnt = 1
    for value in clothes_dict.values():
        cnt *= (value+1)
    return cnt-1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))
