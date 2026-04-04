class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = {}

        for num in nums:
            if num in items:
                return True
            items[num] = items.get(num, 0) + 1

        return False
        