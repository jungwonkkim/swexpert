#백준 16673. 고려대학교에는 공식 와인이 있다...

C, K, P = map(int, input().split())
result = int((C*(C+1)*(K/2))+(C*(C+1)*(P*(2*C+1)/6)))
print(result)