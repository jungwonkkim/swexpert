str_list = input()
counter = 0
blank_flag = True
for char in str_list:
    if char == ' ':
        blank_flag = True
    else:
        if blank_flag:
            counter+=1
            blank_flag = False
print(counter)