class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            s1 = -heapq.heappop(max_heap)
            s2 = -heapq.heappop(max_heap)

            rem = s1 - s2

            heapq.heappush(max_heap, -rem)

        if len(max_heap) > 0:
            return -max_heap[0]
        else:
            return 0