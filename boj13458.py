#백준13458 시험 감독

N = int(input()) #시험장의 개수
A = list(map(int, input().split())) #각 시험장에 있는 응시자의 수
B, C = map(int, input().split()) #총감독, 부감독의 감독가능 응시자 수
cnt = N
for a in A:
    if a <= B:
        continue
    if (a-B)%C:
        cnt += ((a-B)//C)+1
        continue
    cnt += ((a-B)//C)

print(cnt)