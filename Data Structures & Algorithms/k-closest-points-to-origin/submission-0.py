class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for p in points:
            x, y = p
            dist = -math.sqrt(x**2 + y**2)
            # max_heap.append((-dist, x, y))
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, x, y))
            else:
                heapq.heappushpop(max_heap, (dist, x, y))

        return [heapq.heappop(max_heap)[1:3] for _ in range(k)]

        # heapq.heapify(max_heap)
        