#3304. 최장 공통 부분 수열

T = int(input())
for test_case in range(1, T+1):
    stringA, stringB = input().split()
    sub_list = []
    for a in range(len(stringA)):
        i = a
        substring= ''
        searchB = stringB[0:]
        while i < len(stringA):
            for idx, b in enumerate(searchB):
                if stringA[i] == b:
                    substring += b
                    searchB = searchB[idx+1:]
                    i +=1
                    break
            else:
                i += 1
        sub_list.append(len(substring))

        
    for b in range(len(stringB)):
        j = b
        substring= ''
        searchA = stringA[0:]
        while j < len(stringA):
            for aidx, a in enumerate(searchA):
                if stringB[j] == a:
                    substring += a
                    searchA = searchA[aidx+1:]
                    j +=1
                    break
            else:
                j += 1
        sub_list.append(len(substring))
    print('#{} {}'.format(test_case, max(sub_list)))
            