#수 정렬하기2



n = int(input())
n_list = [int(input()) for _ in range(n)]
print("\n".join(map(str,sorted(n_list))))