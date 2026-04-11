class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = defaultdict(int)
        for n in nums:
            h_map[n] += 1

        min_heap = []

        for item, count in h_map.items():
            min_heap.append((count, item))

        heapq.heapify(min_heap)

        while len(min_heap) > k:
            heapq.heappop(min_heap)

        print(min_heap)
        return [item for (count, item) in min_heap]