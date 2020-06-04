"""
프로그래머스 42579 베스트앨범
https://programmers.co.kr/learn/courses/30/lessons/42579
code written by jungwonkkim
"""


def solution(genres, plays):
    answer = []
    genres_dict = {}
    genres_cnt = {}
    for i in range(len(genres)):
        if genres[i] in genres_dict:
            genres_cnt[genres[i]] += plays[i]
            flag = False
            for idx in range(len(genres_dict[genres[i]])):
                if idx > 1:
                    break
                if plays[i] < plays[genres_dict[genres[i]][idx]]:
                    continue
                elif plays[i] == plays[genres_dict[genres[i]][idx]] and i > genres_dict[genres[i]][idx]:
                    continue
                else:
                    genres_dict[genres[i]].insert(idx, i)
                    flag = True
                    break
            if idx == len(genres_dict[genres[i]])-1 and flag == False:
                genres_dict[genres[i]].append(i)
        else:
            genres_cnt[genres[i]] = plays[i]
            genres_dict[genres[i]] = [i]
    genres_cnt_list = sorted(genres_cnt.items(), key=lambda x: x[1], reverse=True)
    print(genres_cnt, genres_dict, genres_cnt_list)
    for genre in genres_cnt_list:
        if len(genres_dict[genre[0]]) ==1:
            answer.append(genres_dict[genre[0]][0])
            continue
        answer.append(genres_dict[genre[0]][0])
        answer.append(genres_dict[genre[0]][1])


    return answer


print(solution(['classic', 'pop', 'classic', 'classic', 'pop', 'pop', 'pop', 'pop','classic', 'pop'],
               [500, 600, 150, 800, 2500, 1000 , 600, 600, 150, 600]))