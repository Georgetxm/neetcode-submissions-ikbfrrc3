class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_map = {}

        for n in nums:
            if n in num_map:
                return n
            else:
                num_map[n] = True