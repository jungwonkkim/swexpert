from copy import deepcopy

def solution(s):
    answer = []
    candidate = [[] for _ in range(501)]
    flag = False
    for idx, char in enumerate(s):
        if idx==0 or idx== len(s)-1:
            continue
        if char == '{':
            flag = True
            number = ''
            element = []
        elif char =='}':
            element.append(int(number))
            candidate[len(element)-1] = deepcopy(element)
            flag = False
        elif char == ',':
            if flag == False:
                continue
            else:
                element.append(int(number))
                number = ''
                continue
        else:
            number+=char
    for can in candidate:
        if can:
            for c in can:
                if c in answer:
                    continue
                else:
                    answer.append(c)
        else:
            break
    return answer