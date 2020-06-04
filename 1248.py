"""
swea 1248 공통조상
code written by jungwonkim
"""

T = int(input())

for test_case in range(1,T+1):
    V, E, num1, num2 = map(int,input().split())
    edges = list(map(int,input().split()))
    children = {}
    parent = {}
    for _ in range(E):
        s = edges.pop(0)
        e = edges.pop(0)
        if s in children:
            children[s].append(e)
        else:
            children[s] = [e]
        parent[e] = s
    ancestors = [[] for _ in range(2)]

    while True:
        if num1 in parent:
            num1 = parent[num1]
            ancestors[0].append(num1)
        if num2 in parent:
            num2 = parent[num2]
            ancestors[1].append(num2)
        if num1 in ancestors[1]:
            root = num1
            break
        if num2 in ancestors[0]:
            root = num2
            break

    deque = [root]
    res = 1
    while deque:
        n = deque.pop(0)
        if n in children.keys():
            for i in children[n]:
                deque.append(i)
                res += 1

    print('#{} {} {}'.format(test_case, root, res))