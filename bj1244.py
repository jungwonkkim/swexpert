#백준1244 [ 스위치 켜고 끄기 ]

def switch (n):
    if n == 1:
        return 0
    if n == 0:
        return 1

n = int(input())
switch_list = list(map(int, input().split()))
s_num = int(input())
for i in range(s_num):
    a, b = map(int, input().split())
    if a ==1:
        for i in range(n):
            if (i+1) % b ==0:
                switch_list[i] = switch(switch_list[i])
    else:
        switch_list[b-1] = switch(switch_list[b-1])
        if b == n or b ==1:
            continue
        elif b>(n/2):
            for i in range(1, n-b+1):
                if switch_list[b-1+i] !=switch_list[b-1-i]:
                    break
                else :
                    switch_list[b-1+i] = switch(switch_list[b-1+i])
                    switch_list[b-1-i] = switch(switch_list[b-1-i])
        else:
            for i in range(1, b):
                if switch_list[b-1+i] != switch_list[b-1-i]:
                    break
                else :
                    switch_list[b-1+i] = switch(switch_list[b-1+i])
                    switch_list[b-1-i] = switch(switch_list[b-1-i])
for i in range(n):
    print(switch_list[i], end = ' ')
    if (i+1)%20 ==0:
        print()
print()
