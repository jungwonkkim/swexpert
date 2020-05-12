"""
백준 17140 이차원 배열과 연산
https://www.acmicpc.net/problem/17140
code written by jungwonkim
"""


def new_sort(arr):
    counter_arr = [[0 , i] for i in range(max(arr)+1)]
    for num in arr:
        counter_arr[num][0] += 1
    counter_arr.sort()
    new_arr = []
    for counter in counter_arr:
        if counter[0] == 0:
            continue
        else:
            new_arr.append(counter[1])
            new_arr.append(counter[0])
    return new_arr[:100]



r, c, k = map(int, input().split())
max_r = 3
max_c = 3
table = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    table[i][0], table[i][1], table[i][2] = map(int, input().split())
cnt = 0
while True:
    if table[r-1][c-1] == k:
        break
    if cnt == 100:
        cnt = -1
        break
    if max_r<=max_c:
        for i in range(100):
            temp_table = [table[i][j] for j in range(100) if table[i][j] !=0]
            if temp_table:
                sorted_table = new_sort(temp_table)
                row = len(sorted_table)
                if max_r < row:
                    max_r = row
                for a in range(row):
                    table[i][a] = sorted_table[a]
                if row <100:
                    for b in range(row, 100):
                        table[i][b] = 0
            else:
                break
    else:
        for i in range(100):
            temp_table = [table[j][i] for j in range(100) if table[j][i] !=0]
            if temp_table:
                sorted_table = new_sort(temp_table)
                column = len(sorted_table)
                if max_c < column:
                    max_c = column
                for a in range(column):
                    table[a][i] = sorted_table[a]
                if column<100:
                    for b in range(column, 100):
                        table[b][i] = 0
            else:
                break
    cnt +=1
print(cnt)