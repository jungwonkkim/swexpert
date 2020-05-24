"""
프로그래머스 코딩테스트 연습
완주하지 못한 선수
code written by jungwonkkim
"""

def solution(participant, completion):
    counter = {}
    for p in participant:
        if p in counter:
            counter[p] +=1
        else:
            counter[p] = 1
    for c in completion:
        counter[c] -=1
        if counter[c] == 0:
            del counter[c]
    for key in counter:
        answer = key
    return answer