symbol = ["+", "-", "*"]

def calculate(idx, arr):
    global max_val
    if idx == N:
        print(arr)
        while len(arr)>3:
            temp = str(eval(arr[0]+arr[1]+arr[2]))
            arr = [temp] + arr[3:]
        if len(arr) == 3:
            res = eval(arr[0]+arr[1]+arr[2])
        else:
            res = int(arr[0])
        print(res)
        if max_val < res:
            max_val = res
    else:
        if numbers[idx] in symbol:
            arr.append(numbers[idx])
            calculate(idx+1, arr)
        else:
            if len(arr)>=3 and arr[-3] == '(':
                new = str(eval(arr[-2]+arr[-1]+ numbers[idx]))
                arr = arr[:-3] + [new]
                calculate(idx+1,arr)
            else:
                arr.append(numbers[idx])
                calculate(idx+1,arr)
                arr.pop()
                if idx != N-1 and arr.count('(') == 0:
                    while len(arr)>5:
                        new = str(eval(arr[0]+arr[1]+arr[2]))
                        arr = [new] + arr[3:]
                    arr.append('(')
                    arr.append(numbers[idx])
                    calculate(idx+1, arr)


N = int(input())
numbers = input()
max_val = -2 ** 31
if N == 1:
    print(max(max_val, int(numbers)))
else:
    Flag = True
    calculate(0, [])
    print(max_val)