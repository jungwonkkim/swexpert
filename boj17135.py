def turn (n)



def attack (num1, num2, num3):
    archery = [num1, num2, num3]
    enemy = 0

    for line in range(N-1, -1, -1):
        




N, M, D = map(int, input().split())
field = [[] for _ in range(N)]
max_kill = 0
for i in range(N):
    field[i] = list(map(int, input().split()))

for arch1 in range(M-2):
    for arch2 in range(arch1+1, M-1):
        for arch3 in range(arch2+1, M):
            kill = attack(arch1, arch2, arch3)
            if kill > max_kill:
                max_kill = kill
print(max_kill)