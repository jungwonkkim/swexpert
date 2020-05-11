def solution(gems):
    gem_dict = {}
    min_left = 100001
    min_right = -1
    left = 0
    for idx, gem in enumerate(gems):
        if gem not in gem_dict:
            gem_dict[gem] = 1
            min_left = left
            min_right = idx
            continue
        else:
            gem_dict[gems[idx]]+=1
            if gem == gems[left]:
                left +=1
            else:
                if gem_dict[gems[left]] ==1:
                    continue
                else:
                    gem_dict[gems[left]] -=1
                    left +=1
            if abs(min_right-min_left) < idx-left:
                min_right = idx
                min_left = left
    answer=[min_left+1, min_right+1]
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

