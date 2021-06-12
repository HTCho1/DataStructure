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
    