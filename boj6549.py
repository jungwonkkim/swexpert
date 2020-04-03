#백준 히스토그램에서 가장 큰 직사각형


while True:
    histogram = list(map(int, input().split()))
    if histogram[0] != 0:
        length = histogram.pop(0)
        max_val = max(length, max(histogram))
        dnc(0, length)
        print(max_val)
    else:
        exit()



