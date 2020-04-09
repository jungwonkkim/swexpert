
class Node:
    def __init__(self,d=0, n = None):
        self.data = d
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def printList(lst):
    if lst.head is None :
        return
    cur = lst.head
    print(lst.size, '[', end=' ')
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next
    print(']')

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

def deleteFirst(lst):
    if lst.head is None:
        return
    lst.head = lst.head.next
    if lst.head is None:
        lst.tail= None
    lst.size -= 1

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = LinkedList()
    num = list(map(int, input().split()))
    for i in range(N):
        insertAt(arr, arr.size, Node(num[i]))
    for i in range(M):
        a, b = map(int, input().split())
        insertAt(arr, a, Node(b))
    for i in range(L):
        deleteFirst(arr)
    print('#{} {}'.format(test_case, arr.head.data))
