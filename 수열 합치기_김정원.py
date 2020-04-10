#swea 5110.py
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
        end = end.prev
    return ans[:-1]

def append(lst, data):
    new_node = Node(data)
    if lst.head is None:
        lst.head = lst.tail = new_node
        return
    lst.tail.next = new_node
    new_node.prev = lst.tail
    lst.tail = new_node
    lst.size +=1


def addList(lst, new_list):
    cur = lst.head
    data = new_list.head.data
    while True:
        if cur.data > data:
            if cur.prev:
                cur.prev.next = new_list.head
                new_list.head.prev = cur.prev
                cur.prev = new_list.tail
                new_list.tail.next = cur
                break
            else:
                cur.prev = new_list.tail
                new_list.tail.next = cur
                lst.head = new_list.head
                break
        elif cur.next:
            cur = cur.next
        else:
            cur.next = new_list.head
            new_list.head.prev = cur
            lst.tail = new_list.tail
            break
    lst.size += new_list.size



T = int(input())
for test_case in range(1, T+1):
    linked = LinkedList()
    N, M = map(int, input().split())
    for i in range(M):
        if i ==0:
            for j in map(int, input().split()):
                append(linked, j)
            continue
        new_linked = LinkedList()
        for j in map(int, input().split()):
            append(new_linked, j)
        addList(linked, new_linked)

    answer = printList(linked)
    print('#{} {}'.format(test_case, answer))



