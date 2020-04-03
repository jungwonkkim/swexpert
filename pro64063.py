def solution(k, room_number):
    answer = []
    vacancy = {}
    for room in room_number:
        if room in vacancy:
            find = room
            child = []
            while True:
                if find in vacancy:
                    find = vacancy[find]
                    child.append(find)
                else:
                    for ch in child:
                        vacancy[ch] = find + 1
                    answer.append(find)
                    break
        else:
            answer.append(room)
            vacancy[room] = room + 1
    return answer

