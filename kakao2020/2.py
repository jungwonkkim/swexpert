operations = ['*', '+', '-']

def divider(exp):
    numstack = ''
    opqueue = []
    numqueue = []
    for num in exp:
        if num.isnumeric():
            numstack += num
        else:
            numqueue.append(int(numstack))
            numstack = ''
            opqueue.append(num)
    numqueue.append(int(numstack))
    return opqueue, numqueue

answer = 0

def calculate(operands, opqueue, op_visited):
    global answer
    if len(op_visited) == 3:
        if operands[0] < 0:
            operands[0] = abs(operands[0])
        if answer < operands[0]:
            answer = operands[0]
        return
    for op in operations:
        if op not in op_visited:
            op_visited.append(op)
            num_stack = []
            new_operands = []
            op_delete = []
            for idx, num in enumerate(operands):
                if num_stack:
                    if op == '*':
                        num1 = num_stack.pop()
                        new_num = num * num1
                        op_delete.append(idx-1)
                        if idx == len(operands) - 1:
                            new_operands.append(new_num)
                            continue
                        if opqueue[idx] == op:
                            num_stack.append(new_num)
                        else:
                            new_operands.append(new_num)
                    elif op == '+':
                        num1 = num_stack.pop()
                        new_num = num + num1
                        op_delete.append(idx-1)
                        if idx == len(operands) - 1:
                            new_operands.append(new_num)
                            continue
                        if opqueue[idx] == op:
                            num_stack.append(new_num)
                        else:
                            new_operands.append(new_num)
                    else:
                        num1 = num_stack.pop()
                        new_num = num1 - num
                        op_delete.append(idx-1)
                        if idx == len(operands) - 1:
                            new_operands.append(new_num)
                            continue
                        if opqueue[idx] == op:
                            num_stack.append(new_num)
                        else:
                            new_operands.append(new_num)
                else:
                    if idx == len(operands)-1:
                        new_operands.append(num)
                        continue
                    if opqueue[idx] == op:
                        num_stack.append(num)
                    else:
                        new_operands.append(num)
            new_operations = []
            for i in range(len(opqueue)):
                if i in op_delete:
                    continue
                else:
                    new_operations.append(opqueue[i])
            calculate(new_operands, new_operations, op_visited)
            op_visited.pop()



def solution(expression):
    ops, numbers = divider(expression)
    calculate(numbers, ops, [])
    return answer

e = "50*6-3*2"
print(solution(e))