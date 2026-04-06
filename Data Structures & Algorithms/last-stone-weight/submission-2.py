class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) >= 2:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            new_stone = -stone1 - -stone2
            
            if new_stone > 0:
                heapq.heappush(max_heap, -new_stone)

        if max_heap:
            return -max_heap[0]
        else:
            return 0
