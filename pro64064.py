from copy import deepcopy
def fit(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        for idx in range(len(s1)):
            if s1[idx] == '*':
                continue
            else:
                if s1[idx] != s2[idx]:
                    return False
    return True


def solution(user_id, banned_id):
    candidate = []
    def dfs(idx, id_set):
        if idx == len(banned_id):
            if id_set in candidate:
                pass
            else:
                candidate.append(deepcopy(id_set))
            return
        for id in user_id:
            if id in id_set:
                continue
            else:
                if fit(banned_id[idx], id):
                    id_set.add(id)
                    dfs(idx+1, id_set)
                    id_set.remove(id)
        return
    dfs(0, set())
    answer = len(candidate)
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))