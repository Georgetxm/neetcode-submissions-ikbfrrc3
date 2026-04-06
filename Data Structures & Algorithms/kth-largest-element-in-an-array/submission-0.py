class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counts = {}
        max_heap = []
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        max_heap = [(-num, count) for num, count in counts.items()]

        heapq.heapify(max_heap)
        last = None

        while k > 0:
            num, count = heapq.heappop(max_heap)
            last = -num
            k -= count

        return last

        
