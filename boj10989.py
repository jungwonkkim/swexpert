counter = [0]* 10001
n= int(input())
for i in range(n):
    counter[int(input())]+=1

for j in range(len(counter)):
    if counter[j] != 0:
        for c in range(counter[j]):
            print(j)