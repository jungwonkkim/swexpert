from itertools import combinations

M = 5
C = 3
closing = list(combinations([n for n in range(M)], C))
print(closing)