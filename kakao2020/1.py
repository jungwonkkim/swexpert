phone = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1]}
def solution(numbers, hand):
    answer = ''
    left_position = [3,0]
    right_position = [3,2]
    for number in numbers:
        if number == 1 or number ==4 or number == 7:
            answer += 'L'
            left_position = phone[number]
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right_position = phone[number]
        else:
            left_dist = abs(phone[number][0] - left_position[0]) + abs(phone[number][1] - left_position[1])
            right_dist = abs(phone[number][0] - right_position[0]) + abs(phone[number][1] - right_position[1])
            if left_dist < right_dist:
                answer+='L'
                left_position = phone[number]
            elif right_dist < left_dist:
                answer += 'R'
                right_position = phone[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_position = phone[number]
                else:
                    answer += 'L'
                    left_position = phone[number]
    return answer

arr = [7,0,8,2,8,3,1,5,7,6,2]
h = 'left'

print(solution(arr, h))