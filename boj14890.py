#백준14890 경사로
def route_making(arr):
    stack = []
    i = -1
    while True:
        i +=1
        if i >= N:
            return True
        if i == 0 or arr[i] ==arr[i-1]:
            stack.append(arr[i])
            continue
        elif arr[i] > arr[i-1]+1 or arr[i]<arr[i-1]-1:
            return False
        elif arr[i] == arr[i-1]+1:
            for j in range(L):
                if stack:
                    if stack.pop() != arr[i]-1:
                        return False
                else:
                    return False
            stack.append(arr[i])
            continue
        elif arr[i] == arr[i-1]-1:
            for j in range(i+1, i+L):
                if j> N-1 or arr[j] != arr[i]:
                    return False
            else:
                i = i+L-1
                continue



N , L = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(N)]
path_rotate = [[path[i][j] for i in range(N)]for j in range(N)]
cnt = 0
for i in range(N):
    if route_making(path[i]):
        cnt+=1
    if route_making(path_rotate[i]):
        cnt+=1

print(cnt)