#백준 14888. 연산자 끼워넣기

def calculate(idx, value):
    global max_val
    global min_val
    global operator
    if idx == N:
        if max_val < value:
            max_val = value
        if min_val > value:
            min_val = value
        return
    if operator[0]:
        operator[0] -=1
        calculate(idx+1, value+num_list[idx])
        operator[0] +=1
    if operator[1]:
        operator[1] -=1
        calculate(idx+1, value-num_list[idx])
        operator[1]+=1
    if operator[2]:
        operator[2] -=1
        calculate(idx+1, value * num_list[idx])
        operator[2] +=1
    if operator[3]:
        operator[3] -=1
        if value<0:
            calculate(idx+1, -(abs(value)//num_list[idx]))
        else:
            calculate(idx+1, value//num_list[idx])
        operator[3] +=1

N = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_val = -1000000000
min_val = 1000000000
calculate(1, num_list[0])
print(max_val)
print(min_val)