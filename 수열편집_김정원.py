class Node:
    def __init__(self, d=0, n = None):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

mylist = LinkedList()



def deleteLast(lst):
    if lst.head is None:
        return
    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next
    if pre is None:
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
    lst.size -=1



def insertAt(lst,idx, new):
    if lst.head is None:
        lst.head = lst.tail = new
    elif idx >= lst.size:
        lst.tail.next = new
        lst.tail = new
    elif idx == 0:
        new.next = lst.head
        lst.head = new
    else:
        pre,cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
    lst.size += 1

def deleteAt(lst, idx):
    i = 0
    cur = lst.head
    pre = None
    nxt = lst.head.next
    if idx == 0:
        lst.head = nxt
    else:
        while i < idx:
            if cur.next:
                pre = cur
                cur = nxt
                nxt = nxt.next
            else:
                break
            i += 1
        if i ==idx:
            pre.next = nxt
        else:
            return -1

T = int(input())
for test_case in range(1, T+1):
    arr = LinkedList()
    N, M, L = map(int, input().split())
    num = list(map(int, input().split()))
    for i in range(N):
        insertAt(arr, arr.size, Node(num[i]))
    for i in range(M):
        command = list(input().split())
        if command[0] == 'D':
            deleteAt(arr, int(command[1]))
        elif command[0] == 'I':
            insertAt(arr, int(command[1]), Node(int(command[2])))
        else:
            deleteAt(arr, int(command[1]))
            insertAt(arr, int(command[1]), Node(int(command[2])))
    for i in range(L):
        deleteAt(arr, 0)
        if arr.head is None:
            break
    if arr.head is None:
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}'.format(test_case, arr.head.data))