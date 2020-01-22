my_str = input()
output =''
for char in my_str:
    numz = ord(char) - 64
    output += str(numz) + ' '
    
print(output)