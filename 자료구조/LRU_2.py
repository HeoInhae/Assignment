class Node:
    def __init__(self, page):
        self.page = page
        self.next = None
        self.prev = None

class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots
        self.cache_hit = 0
        self.tot_cnt = 1
        self.cache_map = {} 
        self.head = None  
        self.tail = None  

    def do_sim(self, page):
        if page in self.cache_map:
            self.cache_hit += 1
            node = self.cache_map[page]
            self._move_to_front(node)
        else:
            if len(self.cache_map) >= self.cache_slots:
                self._remove_lru()
            node = Node(page)
            self.cache_map[page] = node
            self._add_to_front(node)

        self.tot_cnt += 1

    def _move_to_front(self, node):
        if node == self.head:
            return
        self._remove(node)
        self._add_to_front(node)

    def _remove_lru(self):
        if self.tail:
            del self.cache_map[self.tail.page]
            self._remove(self.tail)

    def _remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def _add_to_front(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

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
