#4111. 무선 단속 카메라
#각 카메라 간 거리를 구한 후 수신기-1 만큼 제일 큰 차터 하나씩 없애줄거다.
#이 알고리즘이 맞다면 빠르게 할 수 있을 것 같다.

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    K = int(input())
    dist = 0
    cameras = list(set(list(map(int, input().split())))) #중복되는 카메라 없애기
    if K >= len(cameras): #수신기의 수가 카메라보다 같거나 많으면 수신거리 0
        print('#{} {}'.format(test_case, dist))
        continue
    cameras.sort() #카메라 위치 정렬
    diff = []
    for i in range(len(cameras)-1):
        diff.append(cameras[i+1] - cameras[i]) #각 카메라 거리 차 리스트화
    diff.sort() #차 배열 정렬
    for setting in range(len(diff)-K+1):
        dist += diff[setting]
    print('#{} {}'.format(test_case, dist))



