str_list = input()
new_list = []
max_count = 0
result = ''
for char in str_list:
    new_list.append(char.upper())
word_counter = {}
for char in new_list:
    if char in word_counter:
        word_counter[char] +=1
    else:
        word_counter[char] = 1
for word in word_counter:
    if word_counter[word] > max_count:
        max_count = word_counter[word]
        result = word
    elif word_counter[word] == max_count:
        result = '?'
print(result)