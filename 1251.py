"""
하나로
"""
class Disjointset:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, r1, r2):
        if self.rank[r1] > self.rank[r2]:
            self.parent[r2] = r1
        else:
            self.parent[r1] = r2
            if self.rank[r1] == self.rank[r2]:
                self.rank[r2] +=1

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())
    edges = []
    dj_set = Disjointset(N)
    min_cost = 0
    for i in range(N):
        for j in range(i+1, N):
            e = ((xs[i]-xs[j])**2 + (ys[i]-ys[j])**2)
            edges.append([i, j, e])
    for edge in sorted(edges, key= lambda x:x[2]):
        v, u, cost = edge[0], edge[1], edge[2]
        root1 = dj_set.find(v)
        root2 = dj_set.find(u)
        if root1 != root2:
            dj_set.union(root1, root2)
            min_cost += cost
    print('#{} {}'.format(test_case, format(round(min_cost*E, 0),"10.0f")))
