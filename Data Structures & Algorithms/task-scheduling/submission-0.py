class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        max_heap = []

        for t in tasks:
            counts[t] = counts.get(t, 0) + 1

        max_heap = [-count for count in counts.values()]

        heapq.heapify(max_heap)

        q = deque()
        
        cycles = 0

        while max_heap or q:
            cycles += 1

            if max_heap:
                freq = heapq.heappop(max_heap)
                freq += 1
                if freq < 0:
                    q.append((freq, cycles + n))

            if q and q[0][1] == cycles:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return cycles
