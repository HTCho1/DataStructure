# 한방향 연결리스트 (Singly Linked List)

# 노드 클래스 정의
class Node():
    def __init__(self, key=None, value=None):
        self.key = key      # 노드를 다른 노드와 구분하는 key 값
        self.value = value  # 필요한 경우 추가 데이터 value
        self.next = None    # 다음 노드로의 링크 (초기값은 None)
    def __str__(self): # print(node)인 경우 출력할 문자열
        return str(self.key) # str((self.key, self.value))

class SinglyLinkedList():
    def __init__(self):
        self.head = None   # 연결리스트의 가장 앞의 노드 (head), 초기값은 None
        self.size = 0      # 리스트의 노드 개수 (필요하다면)
    def __iter__(self):    # generator 정의
        v = self.head
        while v != None:   # generator : yield가 있는 함수
            yield v        # yield를 포함한 __iter__라는 메서드를 class 안에 두면
                           # for in : 을 사용할 수 있다.
            v = v.next     # v == None이 되어 while 문을 빠져나오면
                           # StopIterator(Error Message)가 자동적으로 생성되어
                           # for 문을 빠져나온다.
    def __str__(self):     # 연결리스트의 값을 print 출력
        return " -> ".join(str(v) for v in self)
        # generator를 이용해 for 문으로 노드를 순서대로
        # 접근해서 join 함 (key 값 사이에 -> 를 넣어 출력)
    def __len__(self):
        return self.size   # len(A) = A의 노드 개수 리턴
    def pushFront(self, key, value=None): # 현재 head 노드 앞에 새로운 노드를 생성하여 삽입. 삽입된 노드가 새로운 head가 되어야 한다.
        new_node = Node(key, value)  # 새 노드 생성
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    def pushBack(self, key, value=None):
        new_node = Node(key, value)
        if self.size == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None: # tail 노드 찾기
                tail = tail.next
            tail.next = new_node
        self.size += 1
    def popFront(self):     # 리스트의 head 노드를 삭제하고 key 값을 반환
        if self.size == 0:  # or len(self) == 0 -> 빈 리스트
            return None     # return None if it's empty
        else:
            x = self.head
            key = x.key # value = x.value
            self.head = x.next
            self.size = self.size - 1
            del x       # delete x from memory
            return key  # or return (key, value)
    def popBack(self):      # tail 노드를 찾아 지우고 key 값을 반환, tail 노드의 전 노드를 알아야 한다. (전 노드의 링크를 수정해야 하므로)
        if self.size == 0:  # 빈 리스트인 경우 (1)
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if prev == None: # 리스트에 노드가 하나만 있는 경우 (2)
                self.head = None
            else:            # 리스트에 두 개 이상의 노드가 있는 경우 (3)
                prev.next = tail.next # or prev.next = None
            key = tail.key
            del tail
            self.size -= 1
            return key
    def search(self, key):  # key (int) 값을 지정한 노드를 찾아 리턴하고 없으면 None 리턴
        # 방법 1 : head 노드부터 next 링크를 따라가면서 뒤지는 방법
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return v
    '''
    def search(self, key):
        # 방법 2 : for 루프를 이용하는 방법 <- __iter__(self)에 의해 가능!
        for v in self:
            if v.key == key:
                return v
        return None
    '''
    def remove(self, v):
        if self.size == 0 or v == None: return None
        print(type(self.head), type(v), type(self.head.key), type(v.key))
        if v == self.head.key: # type(v) = class '__main__.Node'
                               # type(v.key) = class 'int'
                               # type(self.head) = class '__main__.Node'
                               # type(self.head.key) = class '__main__.Node'
            self.head = self.head.next
            self.size -= 1
            del v
        else:
            prev, next = None, self.head
            while next != None:
                if next.key == v:
                    prev.next = next.next
                    del v
                    self.size -= 1
                    break
                prev = next
                next = next.next
a = Node(3)
b = Node(9)
c = Node(-1)
d = Node(5)
SLL = SinglyLinkedList()

SLL.pushBack(a)
SLL.pushBack(b)
SLL.pushBack(c)
SLL.pushBack(d)
print('SLL: ', SLL)
SLL.remove(c)
print('SLL: ', SLL)
print(SLL.search(3))