class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        
        heapq.heapify(max_heap)
        print(max_heap)

        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)
            diff = s1 - s2

            heapq.heappush(max_heap, diff)
            print(max_heap)

        if max_heap:
            return -max_heap[-1]
        else:
            return 0
