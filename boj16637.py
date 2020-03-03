symbol = ['+','-','*']

def calculate(idx, arr):
    global max_val
    if idx == N:
        while len(arr)>3:
            temp = str(eval(arr[0]+arr[1]+arr[2]))
            arr = [temp] + arr[3:]
        if len(arr) == 3:
            res = eval(arr[0]+arr[1]+arr[2])
        else:
            res = int(arr[0])
        if max_val < res:
            max_val = res
        return
    if numbers[idx] in symbol:
        arr.append(numbers[idx])
        calculate(idx+1, arr)
        arr.pop()
        return
    if len(arr)>=3 and arr[-3] == '(':
        new = str(eval(arr[-2]+arr[-1]+ numbers[idx]))
        if len(arr)>3:
            arr = arr[:-3] + [new]
        else:
            arr = [new]
        calculate(idx+1,arr)
        arr.pop()
        return
    arr.append(numbers[idx])
    calculate(idx+1,arr)
    arr.pop()
    if idx != N-1:
        while len(arr)>2:
            new = str(eval(arr[0]+arr[1]+arr[2]))
            arr = [new] + arr[3:]
        arr.append('(')
        arr.append(numbers[idx])
        calculate(idx+1, arr)
        arr.pop()
        arr.pop()


N = int(input())
numbers = input()
max_val = -2 ** 31
if N == 1:
    print(max(max_val, int(numbers)))
else:
    calculate(0, [])
    print(max_val)