#백준 14501 퇴사

def revenue_making(idx, rev):
    global max_rev
    if idx == N:
        if max_rev < rev:
            max_rev = rev
        return
    revenue_making(idx+1, rev)
    if idx + table[idx][0] <= N:
        revenue_making(idx+table[idx][0], rev+table[idx][1])

N = int(input())
table = []
for i in range(N):
    t, p = map(int, input().split())
    table.append((t,p))
max_rev = 0
revenue_making(0, 0)

print(max_rev)
