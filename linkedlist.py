
class Node:
    def __init__(self,d=0, n = None):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

mylist = LinkedList()

def printList(lst):     #lst : LinkedList 객체의 주소
    if lst.head is None : return
    cur = lst.head
    print(lst.size, '[', end=' ')
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next
    print(']')

#리스트의 마지막에 추가하기 : tail도 포함
def insertLast(lst,new):    #new : 새로추가할 노드 객체
    #빈리스트일 경우
    if lst.head is None:
        lst.head = lst.tail = new   #처음, 마지막 모두 새로운 노드로
    else:   #마지막 노드의 next를 새 노드로
        lst.tail.next = new
        lst.tail = new
    lst.size += 1

#마지막 노드 삭제
def deleteLast(lst):
    if lst.head is None : return    #비어있는리스트면
    pre, cur = None, lst.head   #선행 노드, 현재 노드
    while cur.next is not None:
        pre = cur
        cur = cur.next
    if pre is None :        #리스트 요소가 하나라면
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
    lst.size -= 1

#처음에 원소 삽입하기
def insertFirst(lst,new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1

#처음의 원소 삭제하기
def deleteFirst(lst):
    if lst.head is None: return
    #노드가 1개일 경우
    lst.head = lst.head.next
    if lst.head is None:    #노드가 한개일경우
        lst.tail= None      #테일도 None으로 설정
    lst.size -= 1

#특정 위치에 원소를 저장
def insertAt(lst,idx, new):     #idx : 인덱스값
    #빈리스트일 경우, idx==0일 경우
    if lst.head is None or idx == 0:
        insertFirst(lst,new)
    #마지막에 추가하는 경우 idx >= lst.size일 경우
    elif idx >= lst.size:
        insertLast(lst,new)
    #중간에 추가하는 경우
    else:
        pre,cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
        lst.size += 1

#특정 위치의 원소를 삭제
def deleteAt(lst,idx):
    pass

#삽입
for i in range(5):
    # insertFirst(mylist,Node(i))   #맨앞에 추가
    insertLast(mylist,Node(i))      #맨 뒤에 추가
    printList(mylist)

#삭제
# while mylist.size:
#     # deleteFirst(mylist)   #맨앞의 요소 삭제
#     deleteLast(mylist)      #맨뒤의 요소 삭제
#     printList(mylist)


#특정 위치에 삽입
for i in range(3):
    insertAt(mylist,2,Node(i+10))
    printList(mylist)
#
#특정 위치에 삽입 후 삭제
insertAt(mylist, 6, Node(-1))
printList(mylist)
deleteAt(mylist,6)  #여기는 구현해 보세요!
printList(mylist)


# n5 = Node(5);n4 = Node(4,n5);n3 = Node(3,n4)
# n2 = Node(2,n3);n1 = Node(1,n2)
# mylist.head = n1
# mylist.size = 5
# printList(mylist)