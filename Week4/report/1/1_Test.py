

class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots
        self.cache_hit = 0
        self.tot_cnt = 0
        self.cache = []
        
    def do_sim(self, page):
        self.tot_cnt += 1
        if page in self.cache:
            # 페이지가 캐시에 이미 있으면, 캐시 히트이며, 해당 페이지를 캐시의 끝으로 이동 -> python 내부에서 append 를 어떻게 최적화 할지는 모르지만 만약 [] 가 C++ 기준 배열이라면, 비효율적인 동작, 만약 연결 리스트 방식이면, 그나마 효율이 있다
            self.cache_hit += 1
            self.cache.append(self.cache.pop(self.cache.index(page)))
        else:
            # 페이지가 캐시에 없으면, 새로운 페이지를 추가
            if len(self.cache) >= self.cache_slots:
                # 캐시가 가득 차 있으면, 가장 오래된 페이지(리스트의 첫 번째 요소)를 제거 -> 이 역시 동일하게 효율이 아쉽다.(내부 구현을 모르기에 어떻게 작동하는지를 모르겠음)
                self.cache.pop(0)
            self.cache.append(page)
        
    def print_stats(self):
        print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = ", self.cache_hit / self.tot_cnt)


if __name__ == "__main__":

    data_file = open("C:/Users/me/Desktop/ssu/2-1/DS/Week4/report/1/linkbench.trc")
    lines = data_file.readlines()
    for cache_slots in range(100, 1001, 100):
        cache_sim = CacheSimulator(cache_slots)
        for line in lines:
            page = line.split()[0]
            cache_sim.do_sim(page)
        
        cache_sim.print_stats()

