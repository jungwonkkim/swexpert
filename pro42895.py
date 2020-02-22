#프로그래머스 42895 N으로 표현

"""
DP이니까 사실 2가 필요한건 1 연산 1 아니면 0플러스 2
3개로 할 수 있는 건 1 연산 2 0연산 3
4개로 할 수 있는 건 2 연산 2 1 연산 3 0연산 4 이런..이런 식으로 계산하다가 잭팟나오면
"""


def solution(N, number):
    number_set = [set() for _ in range(8)]
    for i,x in enumerate(number_set, start=1):
        x.add(int(str(N) * i)) #set이기 때문에 append가 아닌 add를 넣어줘야함
    for i in range(1,9):
        for j in range(i):
            for op1 in number_set[j]:
                for op2 in number_set[i-j-1]:
                    number_set[i].add(op1+op2)
                    number_set[i].add(op1-op2)
                    number_set[i].add(op1 * op2)
                    if op2 != 0 and op1%op2 == 0:
                        number_set[i].add(op1//op2)
        if number in number_set[i] :
            answer = i+1
            break
    else:
        answer = -1


    return answer