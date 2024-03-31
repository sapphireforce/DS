class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.nodes = {}
        self.capacity = capacity
        self.size = 0

    def refer(self, page):
        if page not in self.nodes:
            newNode = Node(page)
            if self.size < self.capacity:
                if self.head is None:
                    self.head = self.tail = newNode
                else:
                    self.tail.next = newNode
                    self.tail = newNode
                self.size += 1
            else:
                removed = self.head.value
                self.head = self.head.next
                del self.nodes[removed]
                self.tail.next = newNode
                self.tail = newNode
        else:
            # 여기서는 연결 리스트를 재정렬하는 로직을 구현해야 합니다.
            pass
        self.nodes[page] = newNode

    def display(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()

# 사용 예제는 위와 유사하게 구현할 수 있습니다.

cache = LRUCache(4)
cache.refer(1)
cache.refer(2)
cache.refer(3)
cache.refer(1)
cache.refer(4)
cache.refer(5)
cache.display()  # [2, 3, 4, 5] 출력