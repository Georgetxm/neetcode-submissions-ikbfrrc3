class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_set = {}

        for task in tasks:
            hash_set[task] = hash_set.get(task, 0) + 1

        maxheap = [-cycle for cycle in hash_set.values()]
        
        heapq.heapify(maxheap)

        q = deque()

        clock = 0

        while maxheap or q:
            clock += 1

            if maxheap:
                freq = heapq.heappop(maxheap)

                freq += 1

                if freq < 0:
                    q.append((freq, clock + n))

            if q and q[0][1] == clock:
                heapq.heappush(maxheap, q.popleft()[0])

        return clock

        