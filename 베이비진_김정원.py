"""
swea 5203 베이비진
code written by jungwonkkim
"""

def istriplet(arr):
    if len(arr) <3:
        return False
    card = arr[-1]
    flag = 0
    for idx in range(len(arr)):
        if arr[idx] == card:
            flag +=1
    if flag ==3:
        return True
    else:
        return False

def isrun(arr):
    if len(arr)<3:
        return False
    card = arr[-1]
    if card+1 in arr:
        if card+2 in arr or card-1 in arr:
            return True
    if card-2 in arr and card-1 in arr:
        return True
    return False


T = int(input())
for test_case in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    ans = 0
    for i in range(12):
        if i%2:
            player2.append(cards[i])
            if istriplet(player2) or isrun(player2):
                ans = 2
                break
        else:
            player1.append(cards[i])
            if istriplet(player1) or isrun(player1):
                ans = 1
                break
    print('#{} {}'.format(test_case, ans))