#2105. [모의 SW 역량테스트] 디저트 카페

def C_wise_SquareMaking(a, b):
    global max_val
    if (a, b) == (0,0) or (a, b) == (0, N-1) or (a, b) == (N-1, 0) and (a, b) ==(N-1, N-1):
        return
    f_dessert = [cafe[a][b]]
    f_route = [(a,b)]
    cnt = 1
    while True:
        newa = a + cnt
        newb = b + cnt
        if -1<newa<N and -1<newb<N and cafe[newa][newb] not in f_dessert:
            f_route.append((newa,newb))
            f_dessert.append(cafe[newa][newb])
            cnt+=1
        else:
            break
    if cnt>1:
         for scnt in range(f_route[0][1], 0, -1):
            for second in range(len(f_route), 1, -1):
                temp_route = f_route[:second]
                temp_dessert = f_dessert[:second]
                second_route = []
                second_dessert = []
                for r in temp_route:
                    newa = r[0] + scnt
                    newb = r[1] - scnt
                    if -1<newa<N and -1<newb<N and cafe[newa][newb] not in temp_dessert+second_dessert:
                        second_route.append((newa, newb))
                        second_dessert.append(cafe[newa][newb])
                if len(second_route) != second:
                    continue
                else:
                    third_dessert = []
                    tcnt = 1
                    while True:
                        thirda = temp_route[0][0] + tcnt
                        thirdb = temp_route[0][1] - tcnt
                        fourtha = temp_route[-1][0] + tcnt
                        fourthb = temp_route[-1][1] - tcnt
                        if thirda == second_route[0][0]:
                            dessert_val = len(second_dessert)*2 + len(third_dessert)
                            if max_val < dessert_val:
                                max_val = dessert_val
                            break
                        if -1<thirda<N and -1<thirdb<N and cafe[thirda][thirdb] not in temp_dessert+second_dessert + third_dessert:
                            third_dessert.append(cafe[thirda][thirdb])
                        else:
                            break
                        if -1<fourtha<N and -1<fourthb< N and cafe[fourtha][fourthb] not in temp_dessert+second_dessert + third_dessert:
                            third_dessert.append(cafe[fourtha][fourthb])
                        else:
                            break
                        tcnt +=1


T =int(input())
for test_case in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    max_val = -1
    for x in range(N):
        for y in range(N):
            C_wise_SquareMaking(x,y)
    print('#{} {}'.format(test_case, max_val))



