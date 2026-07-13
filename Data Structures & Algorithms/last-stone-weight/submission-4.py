class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            s1 = -heapq.heappop(maxheap)
            s2 = -heapq.heappop(maxheap)

            rem = s1 - s2

            if rem > 0:
                heapq.heappush(maxheap, -rem)

        if len(maxheap) > 0:
            return -maxheap[-1]
        else:
            return 0