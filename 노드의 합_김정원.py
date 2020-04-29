class Tree:
    def __init__(self, node):
        self.tree = [0] * (node + 1)
        self.node = node

    def put(self, x, y):
        self.tree[x] = y

    def search_leaf(self, node):
        if node * 2 > N:
            self.sum += self.tree[node]
        else:
            self.search_leaf(node * 2)
            if node * 2 != N:
                self.search_leaf(node * 2 + 1)

    def sum_making(self, L):
        self.sum = 0
        self.search_leaf(L)
        return self.sum


T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    t = Tree(N)
    for _ in range(M):
        a, b = map(int, input().split())
        t.put(a, b)
    print('#{} {}'.format(test_case, t.sum_making(L)))
