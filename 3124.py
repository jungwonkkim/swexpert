from heapq import heapify, heappop, heappush

def prim(start_node):
    result = 0
    connected_nodes = set(start_node)
    candidate_edge_list = graph[start_node]
    heapify(candidate_edge_list)
    while candidate_edge_list:
        weight, nxt = heappop(candidate_edge_list)
        if nxt not in connected_nodes:
            connected_nodes.add(nxt)
            result += weight
            for edge in graph[nxt]:
                if edge[1] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return result


T  = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    for i in range(E):
        s, e, w = map(int, input().split())
        s = str(s)
        e = str(e)
        if s in graph:
            graph[s].append((w, e))
        else:
            graph[s] = [(w, e)]
        if e in graph:
            graph[e].append((w, s))
        else:
            graph[e] = [(w, s)]
    print(graph)
    res = prim('1')
    print('#{} {}'.format(test_case, res))