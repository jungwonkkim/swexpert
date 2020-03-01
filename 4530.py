#4530. 극한의 청소 작업

def cnt(num):
    result = 0
    n = str(num)
    s = 0
    for i in range(len(n)-1, -1, -1):
        if int(n[i]) > 4:
            result += (int(n[i])-1) * (9**s)
        else:
            result += (int(n[i])) * (9**s)
        s += 1
    return result - 1

T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    if a < 0 and b > 0:
        print("#{} {}".format(test_case, cnt(abs(a)) + cnt(abs(b)) + 1))
    else:
        print("#{} {}".format(test_case, abs(cnt(abs(a)) - cnt(abs(b)))))