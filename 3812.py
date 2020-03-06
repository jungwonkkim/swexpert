# 3812. 호중이의 큐브색칠

def vector_find(ori, sub, arr):
    q = (sub + 1) // N + (ori - sub) // N
    ra = (sub + 1) % N
    rb = (ori - sub) % N
    for i in range(N):
        if i == 0:
            arr[i] = q - 1
        else:
            arr[i] = q
        if i % N < ra:
            arr[i] += 1
        if i % N < rb:
            arr[i] += 1
    return arr


T = int(input())
for test_case in range(1, T + 1):
    X, Y, Z, A, B, C, N = map(int, input().split())
    X_vector = vector_find(X, A, [0] * N)
    Y_vector = vector_find(Y, B, [0] * N)
    Z_vector = vector_find(Z, C, [0] * N)
    temp = [0] * N
    ans_list = [0] * N
    for i in range(N):
        for j in range(N):
            temp[i] += X_vector[j] * Y_vector[(N + i - j) % N]

    for i in range(N):
        for j in range(N):
            ans_list[i] += temp[j] * Z_vector[(N + i - j) % N]

    ans_list = [str(an) for an in ans_list]
    ans = ' '.join(ans_list)
    print('#{} {}'.format(test_case, ans))
