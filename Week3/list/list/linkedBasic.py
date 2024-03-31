# linkedListBasic.py update
from listNode import ListNode

class LinkedListBasic: #-> 이거 너무 어려운데?? 정확하게 동작하는지도 모르겠네.. ㅋㅋ
    def __init__(self):
        self.head = None
        
    def append(self, item):
        new_node = ListNode(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def insert(self, position, item):
        new_node = ListNode(item)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("OUTOFRANGE")
                current = current.next
            new_node.next = current.next
            current.next = new_node
            
    def pop(self, position=None):
        if (self.head is None):
            raise IndexError("EMPTY")
        if position is None or position == -1:
            if self.head.next is None:  
                item = self.head.item
                self.head = None
                return item
            current = self.head
            while current.next.next:  
                current = current.next
            item = current.next.item  
            current.next = None
            return item
        else:
            if position == 0:
                item = self.head.item
                self.head = self.head.next
                return item
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError("OUTOFRANGE")
                current = current.next
            if current.next is None:
                raise IndexError("OUTOFRANGE")
            item = current.next.item
            current.next = current.next.next
            return item
            
    def __iter__(self):
        current = self.head
        while current:
            yield current.item
            current = current.next
    
    def sort(self):
        if self.head is None or self.head.next is None:
            return 

        made_swaps = True
        while made_swaps:
            made_swaps = False
            current = self.head
            while current.next is not None:
                if current.item > current.next.item:
                    current.item, current.next.item = current.next.item, current.item
                    made_swaps = True
                current = current.next

    def printList(self):
        current = self.head
        while current:
            print(current.item, end=' ')
            current = current.next
        print()