class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots  
        self.cache_hit = 0
        self.tot_cnt = 1
        self.cache_map = {}  
        self.cache_list = []  

    def do_sim(self, page):
        if page in self.cache_map:
            self.cache_hit += 1 
            index = self.cache_map[page] 
            self._move_to_front(index)
        else:
            if len(self.cache_map) >= self.cache_slots:
                self._remove_lru()
            
            self.cache_map[page] = len(self.cache_list)
            self.cache_list.append(page)

        self.tot_cnt += 1

    def _move_to_front(self, index):
        page = self.cache_list.pop(index)
        self.cache_list.insert(0, page) 
        for key, value in self.cache_map.items(): 
            if value < index: 
                self.cache_map[key] += 1 
        self.cache_map[page] = 0

    def _remove_lru(self):
        lru_page = self.cache_list.pop()
        del self.cache_map[lru_page]

    def print_stats(self):
        print("cache_slot =", self.cache_slots, "cache_hit =", self.cache_hit, "hit ratio =", self.cache_hit / self.tot_cnt)


if __name__ == "__main__":
    data_file = open("./linkbench.trc")
    lines = data_file.readlines() 
    for cache_slots in range(100, 1001, 100):
        cache_sim = CacheSimulator(cache_slots) 
        for line in lines: 
            page = line.split("\n")[0]
            cache_sim.do_sim(page) 
        cache_sim.print_stats()
