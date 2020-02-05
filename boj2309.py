#백준 2309. 일곱 난쟁이

dwarf= [int(input())for _ in range(9)]
dwarf.sort()
height = sum(dwarf)-100
for tall in range(8, 0, -1):
    if height - dwarf[tall] > 0:
        for short in range(tall):
            if dwarf[tall] + dwarf[short] == height:
                fraud = [tall, short]
                break
    if fraud:
        break

del dwarf[fraud[0]]
del dwarf[fraud[1]]
for real in dwarf:
    print(real)
