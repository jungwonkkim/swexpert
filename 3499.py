#3499. 퍼펙트 셔플


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    if n %2:
        half = int((n+1)/2)
    else:
        half = int(n/2)
    card_deck = list(input().split())
    left_deck = card_deck[:half]
    right_deck = card_deck[half:]
    card_deck = []
    for i in range(half-1):
        card_deck.append(left_deck[i])
        card_deck.append(right_deck[i])
    if n%2:
        card_deck.append(left_deck[half-1])
    else:
        card_deck.append(left_deck[half-1])
        card_deck.append(right_deck[half-1])
    print(f'#{test_case}', end = ' ')
    for card in card_deck:
        print(card, end = ' ')
    print()
                         