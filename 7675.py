#7675. 통역사 성경이

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    sentence = list(input().split())
    counter = []
    n_counter = 0
    for word in sentence:
        if word[-1]=='!' or word[-1]=='?' or word[-1] =='.':
            if word[:-1].isalpha():
                if word[0].isupper() and word[1:-1].islower():
                    n_counter +=1
            counter.append(n_counter)
            n_counter =0
        else:
            if word.isalpha():
                if len(word)==1:
                    if word.isupper():
                        n_counter+=1
                elif word[0].isupper() and word[1:].islower():
                    n_counter+=1
    print(f'#{test_case}', end= ' ')
    for i in range(len(counter)):
        print(counter[i], end = ' ')
    print()
            