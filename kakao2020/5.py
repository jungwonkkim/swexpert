adjacent_dict = {}
route = {}
degree = {}
answer = True


def route_making(s, e):
    global route
    global answer
    for p in adjacent_dict[s]:
        if s in route[p]:
            answer = False
            return
        route[s].append(p)
        if p == e:
            return
        else:
            route_making(p, e)
        route[s].pop()


def solution(n, path, order):
    global adjacent_dict
    global route
    global answer
    global degree
    answer = True
    adjacent_dict = {i:[] for i in range(n)}
    route = {i:[] for i in range(n)}
    degree = {i:0 for i in range(n)}
    max_degree = 0
    for p in path:
        adjacent_dict[p[0]].append(p[1])
        adjacent_dict[p[1]].append(p[0])
        degree[p[0]] +=1
        degree[p[1]] +=1
        if degree[p[0]] > degree[max_degree]:

    for o in order:
        route_making(o[0], o[1])
    return answer



print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[8,5],[6,7],[4,1]]))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[4,1],[8,7],[6,5]] ))