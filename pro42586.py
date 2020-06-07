"""
프로그래머스 42586 기능개발
https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
code written by jungwonkkim
"""

def solution(progresses, speeds):
    answer = []
    while progresses:
        total = 1
        progress = progresses.pop(0)
        speed = speeds.pop(0)
        days = (100 - progress)//speed + 1
        while True:
            if progresses:
                p = progresses[0]
                s = speeds[0]
                if p + (s*days) >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    total += 1
                else:
                    answer.append(total)
                    break
            else:
                answer.append(total)
                break
    return answer


print(solution([93,30,55], [1,30,5]))