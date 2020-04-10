#swea 5120.py
#code written by jungwonkkim

class Node:
    def __init__(self, d=0, n = None):
        self.data = d
        self.next = n
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

def printList(lst):
    if lst.tail is None:
        return
    ans = ''
    end = lst.tail
    for _ in range(10):
        if end is None:
            break
        ans += str(end.data)+' '
        if end.prev == lst.tail:
            break
        end = end.prev
    return ans[:-1]


def append(lst, data):
    new_node = Node(data)
    if lst.head is None:
        lst.head = lst.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node
        return
    new_node.prev = lst.tail
    new_node.next = lst.head
    lst.tail.next = new_node
    lst.head.prev = new_node
    lst.tail = new_node
    lst.size +=1

def insert(lst, idx, counter):
    cur = lst.head
    cnt = 0
    while cnt < counter:
        for _ in range(idx):
            cur = cur.next
        new_node = Node()
        if cur == lst.head:
            lst.tail = new_node
        new_node.data = cur.data + cur.prev.data
        new_node.next = cur
        new_node.prev = cur.prev
        cur.prev.next = new_node
        cur.prev = new_node
        new_node.next = cur
        cur = new_node
        cnt +=1
    return

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = LinkedList()
    for i in map(int, input().split()):
        append(arr, i)
    insert(arr, M, K)
    print('#{} {}'.format(test_case, printList(arr)))

