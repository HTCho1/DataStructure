# 원형 연결 리스트
class Node():
    def __init__(self, key=None):
        self.key = key
        self.next = None
    def __str__(self):
        return str(self.key)

class CircularLinkedList():
    def __init__(self):
        self.head = Node('head')
        self.head.next = self.head
        self.size = 0
    def __iter__(self):
        v = self.head
        while v.next != self.head:
            yield v
            v = v.next

    def __str__(self):
        return " -> ".join(str(v) for v in self)

    def __len__(self):
        return self.size

    def insert(self, v, key):  # 데이터가 key 값인 노드를 생성하고 현재 노드 다음에 삽입
        new_node = Node(key)
        cur_node = self.find(v)
        new_node.next = cur_node.next
        cur_node.next = new_node
        self.size += 1

    def find(self, v):         # 현재 노드를 찾는다
        cur_node = self.head
        while cur_node.key != v:
            cur_node = cur_node.next
        return cur_node

    def find_previous(self, v):  # 이전 노드를 찾는다.
        cur_node = self.head
        while cur_node.next.key != v:
            cur_node = cur_node.next
        return cur_node

    def remove(self, v):  # 노드 v를 제거한다.
        prev_node = self.find_previous(v)
        prev_node.next = prev_node.next.next
        self.size -= 1

    def show(self):
        cur_mode = self.head
        while cur_mode.next.key != 'head':
            print(cur_mode.key, end=' -> ')
            cur_mode = cur_mode.next
        print(cur_mode.key)

CLL = CircularLinkedList()
CLL.show()
CLL.insert('head', '2')
CLL.show()
CLL.insert('2', '4')
CLL.show()
CLL.insert('4', '5')
CLL.show()
print(len(CLL))
CLL.insert('5', '6')
CLL.show()
CLL.insert('5', '12')
CLL.show()
CLL.remove('2')
CLL.show()
print(len(CLL))
CLL.remove('4')
CLL.show()
CLL.remove('5')
CLL.show()
print(len(CLL))