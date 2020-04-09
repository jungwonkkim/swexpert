class Node:
    def __init__(self, d=0, n = None):
        self.data = d
        self.next = n

    def __del__(self):
        print(self.data, '삭제')


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_data = 0
        self.current = None
        self.before = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.num_of_data +=1

    def delete(self):
        pop_data = self.current.data
        if self.current == self.tail:
            self.tail = self.before
        self.before.next = self.current.next
        self.current = self.before
        self.num_of_data -=1
        return pop_data

    def first(self):
        if self.num_of_data == 0:
            return None
        self.before = self.head
        self.current = self.head.next
        return self.current.data

    def insert(self, idx, node):
        new_node = Node(data, idx)


    def next(self):
        if self.current.next == None:
            return None
        self.before = self.current
        self.current = self.current.next
        return self.current.data
    def size(self):
        return self.num_of_data



def printList(lst):
    cur=lst.head
    print(cur.data)