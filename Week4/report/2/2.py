class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None
        self.index = {}
    
    def append(self, value):
        if value in self.index:
            self.move_to_end(value)#끝으로 이동
        else:
            NewNode = Node(value)
            if not self.tail: #없으면 새로 만들어주기
                self.tail = NewNode
                self.tail.next = NewNode
            else: #아니면 꼬리 물어주기
                NewNode.next = self.tail.next
                self.tail.next = NewNode
                self.tail = NewNode
            self.index[value] = NewNode
            
    def remove_Oldest(self):
        if not self.tail:
            return None
        Oldest = self.tail.next
        if Oldest == self.tail:
            self.tail = None
        else:
            self.tail.next = Oldest.next
        del self.index[Oldest.value] #지우기(중요 -> 버그 발생 지역 예상)
        return Oldest.value
    
    def move_to_end(self, value): #버그 다발 지역(ㅎㅎㅎ)
        if value in self.index and self.index[value] != self.tail:
            node = self.index[value]
            if node.next == self.tail.next:
                self.tail = node
            else:
                prev_node = self._get_prev_node(node) 
                prev_node.next = node.next
                node.next = self.tail.next
                self.tail.next = node
                self.tail = node
#------------------------------------------------------------#
    def _get_prev_node(self, node):
        current = self.tail
        while current and current.next != node:
            current = current.next
        return current
#------------------------------------------------------------#

class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots
        self.cache_hit = 0
        self.tot_cnt = 0
        self.cache = CircularLinkedList() #왜 안되는겨? -> 한참을 찾았네
        
    def do_sim(self, page):
        self.tot_cnt += 1
        if page in self.cache.index:
            self.cache_hit += 1
        else:
            if len(self.cache.index) >= self.cache_slots:
                self.cache.remove_Oldest()
        self.cache.append(page)
        
    def print_stats(self):
        hit_ratio = self.cache_hit / self.tot_cnt if self.tot_cnt > 0 else 0
        print(f"cache_slot = {self.cache_slots}, cache_hit = {self.cache_hit}, hit ratio = {hit_ratio:.4f}")

if __name__ == "__main__":

    data_file = open("C:/Users/me/Desktop/ssu/2-1/DS/Week4/report/2/lru_sim/linkbench.trc")
    lines = data_file.readlines()
    for cache_slots in range(100, 1001, 100):
        cache_sim = CacheSimulator(cache_slots)
        for line in lines:
            page = line.split()[0]
            cache_sim.do_sim(page)
        
        cache_sim.print_stats()
#근데 hit rate가 이정도 나오는게 맞나? 모르겠네
