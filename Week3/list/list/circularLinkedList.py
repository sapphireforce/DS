from listNode import ListNode

class CircularLinkedList: #-> 이거 너무 어려운데?? 정확하게 동작하는지도 모르겠네.. ㅋㅋ
    def __init__(self):
        self.tail = None

    def append(self, item):
        new_node = ListNode(item)
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node  # 꼬리물기
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node # 꼬리물기

    def insert(self, position, item):
        new_node = ListNode(item)
        if not self.tail:  # 텅 비어있다
            self.append(item)
            if position == 0:  # 꼬리물기 -> Circular 만족
                self.tail = new_node
        else:
            current = self.tail.next
            for _ in range(position - 1):
                current = current if current.next != self.tail.next else None
                if not current:
                    break
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if current == self.tail:
                self.tail = new_node  # 꼬리물기 -> Circular 만족

    def pop(self, position=None): #C++로 짜면 이보다 더 직관적으로 만들 자신 있는데, 너무 어렵네
        if not self.tail:
            raise IndexError("EMPTY")
        if self.tail.next == self.tail: #원소가 하나일때
            item = self.tail.item
            self.tail = None
            return item
        if position in [None, -1]:  #마지막 원소 삭제
            current = self.tail.next
            while current.next != self.tail:
                current = current.next
            item = self.tail.item
            current.next = self.tail.next
            self.tail = current
            return item
        current, prev = self.tail.next, self.tail
        for _ in range(position):
            prev, current = current, current.next
            if current == self.tail.next:  
                break
        item = current.item
        prev.next = current.next
        if current == self.tail:  
            self.tail = prev
        return item

    def sort(self):
        if not self.tail or self.tail.next == self.tail:
            return
        did_swap = True
        while did_swap:
            did_swap = False
            current = self.tail.next
            while current != self.tail:
                next_node = current.next
                if current.item > next_node.item: #가장 간단한(?) 정렬 함수
                    current.item, next_node.item = next_node.item, current.item
                    did_swap = True
                current = next_node

    def printList(self):
        if not self.tail:
            print("EMPTY")
            return
        current = self.tail.next
        while True:
            print(current.item, end=' ')
            current = current.next
            if current == self.tail.next:
                break
        print()

    def __iter__(self):
        current = self.tail.next if self.tail else None
        while current:
            yield current.item
            current = current.next if current.next != self.tail.next else None
