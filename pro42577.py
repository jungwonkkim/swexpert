"""
프로그래머스 42577 . 전화번호목록
https://programmers.co.kr/learn/courses/30/lessons/42577
code written by jungwonkkim
"""


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.end = False


class Trie(object):
    def __init__(self, string):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
        cur_node.data = string
        cur_node.end = True

    def search(self, string):
        cur_node = self.head
        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
                if cur_node.end:
                    return True
            else:
                return False
        return True


def solution(phone_book):
    phone_book.sort(key=len)
    trie_dict = {}
    for phone_number in phone_book:
        if phone_number[0] in trie_dict:
            trie = trie_dict[phone_number[0]]
            if trie.search(phone_number):
                return False
            else:
                trie.insert(phone_number)
        else:
            trie_dict[phone_number[0]] = Trie(phone_number[0])
            trie_dict[phone_number[0]].insert(phone_number)
    return True