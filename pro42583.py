
"""
프로그래머스 다리를 지나는 트럭
https://programmers.co.kr/learn/courses/30/lessons/42583
code written by jungwonkkim
"""
def solution(bridge_length, weight, truck_weights):
    total = 0
    temp = []
    time = 0
    while truck_weights and total+truck_weights[0] <= weight:
        time += 1
        a = truck_weights.pop(0)
        total += a
        temp.append((a, time))
        # print(temp)
    if truck_weights:
        while truck_weights:
            while temp and total + truck_weights[0] > weight:
                time = max(bridge_length + temp[0][1], time)
                total -= temp[0][0]
                temp.pop(0)
                # print(temp)
            while truck_weights and total + truck_weights[0] <= weight:
                a = truck_weights.pop(0)
                total += a
                temp.append((a, time))
                time += 1
                # print(temp)
        return temp[-1][1] + bridge_length
    else:
        time += bridge_length
        return time

