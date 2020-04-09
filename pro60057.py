answer = 1001

def dfs(idx, length, string):
    global answer
    if idx+length > len(string)-length:
        if answer > len(string):
            answer = len(string)
        return
    if string[idx:idx+length] == string[idx+length:idx+(2*length)]:
        if idx >=1 and string[idx-1].isnumeric():
            new_string = string[:idx-1] + str(int(string[idx-1])+1) + string[idx+length:]
            dfs(idx, length, new_string)
        else:
            dfs(idx, length+1, string)
            new_string = string[:idx] + '2' + string[idx+length:]
            dfs(idx+1, length, new_string)
    else:
        if idx >= 1 and string[idx-1].isnumeric():
            dfs(idx+length, 1, string)
        else:
            dfs(idx, length+1, string)
            dfs(idx+1, 1, string)

def solution(s):
    dfs(0, 1, s)
    return answer


print(solution('aabbaccc'))