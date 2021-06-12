# 양방향 (원형) 연결리스트 (Circularly Doubly Linked List)

class Node():
    def __init__(self, key=None):
        self.key = key                 # 노드에 저장되는 key 값
        self.next = self.prev = self   # 자기로 향하는 링크
    def __str__(self):                 # print(node)인 경우 출력할 문자열
        return str(self.key)           # or return str(self.key, self.value)

#  양방향(원형) 연결 리스트 클래스
class DoublyLinkedList():
    def __init__(self):
        self.head = Node('head')  # 빈 리스트는 dummy node만으로 표현
        self.size = 0       # 필요하다면
    def __iter__(self):
        v = self.head
        while v.next != self.head:
            yield v
            v = v.next
    def __str__(self):
        return " -> ".join(str(v) for v in self)
    def __len__(self):
        return self.size
    def splice(self, a, b, x):
        #print(type(a), type(b), type(x))
        # 노드 a 부터 노드 b 까지를 떼어내(cut) 노드 x 뒤에 붙여(paste) 넣는 연산
        # cut-and-paste 연산이라고 기억하자
        if a == None or b == None or x == None:
            return
        ap = a.prev      # ap is previous node of a (ap는 a의 이전 노드)
        bn = b.next      # bn is next node of b (bn은 b의 다음 노드)

        # cut [a, ..., b]
        ap.next = bn
        bn.prev = ap
        # insert [a, ..., b] after x
        xn = x.next
        xn.prev = b
        b.next = xn
        a.prev = x
        x.next = a
    def isEmpty(self):
        if self.size == 0: return True
        else: return False
    def search(self, key): # key 값을 갖는 노드를 리턴하고, 없으면 None 리턴
        v = self.head # dummy node
        while v.next != self.head: # 한바퀴를 도는 연산
            if str(v.key) == str(key): return v
            v = v.next
        return None
    def moveAfter(self, a, x): # 노드 a를 노드 x 뒤로 이동
        self.splice(a, a, x)

    def moveBefore(self, a, x): # 노드 a를 노드 x 앞으로 이동
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key): # 노드 x 뒤에 데이터가 key 인 새 노드를 생성해 삽입
        self.size += 1
        self.moveAfter(Node(key), x)

    def insertBefore(self, x, key): # 노드 x 앞에 데이터가 key 인 새 노드를 생성해 삽입
        self.size += 1
        self.moveBefore(Node(key), x)

    def pushFront(self, key): # 데이터가 key 인 새 노드를 생성해 head (dummy) 다음(front)에 삽입
        self.insertAfter(self.head, key)

    def pushBack(self, key): # 데이터가 key 인 새 노드를 생성해 head 이전 (back)에 삽입
        self.insertBefore(self.head, key)

    def remove(self, x): # 노드 x를 제거
        if x == None or x == self.head:
            return
        # x를 떼어냄
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1
        del x

    def popFront(self): # head 다음에 있는 노드의 데이터 값 리턴. 빈 리스트이면 None 리턴
        if self.isEmpty(): return None
        key = self.head.next.key
        self.remove(self.head.next)
        return key

    def popBack(self): # head 이전에 있는 노드의 데이터 값 리턴. 빈 리스트면 None 리턴
        if self.isEmpty(): return None
        key = self.head.prev.key
        self.remove(self.head.prev)
        return key

    def show(self):
        cur_node = self.head
        while cur_node.next.key != 'head':
            print(cur_node.key, end=' -> ')
            cur_node = cur_node.next
        print(cur_node.key)

a = Node(3)
b = Node(9)
c = Node(-1)
d = Node(5)

DLL = DoublyLinkedList()
DLL.show()
DLL.pushFront('3')
DLL.show()
DLL.pushBack('5')
DLL.show()
DLL.pushFront(9)
DLL.show()
DLL.pushFront(-1)
DLL.show()
DLL.popBack()
DLL.show()
DLL.popFront()
DLL.show()
DLL.popFront()
DLL.show()
DLL.pushFront('1')
DLL.show()
#DLL.pushBack(5)
#print(DLL)
#print(DLL.popBack())
#print(DLL)