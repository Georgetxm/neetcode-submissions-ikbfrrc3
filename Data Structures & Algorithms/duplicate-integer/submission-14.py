class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_map = {}

        for num in nums:
            if num in n_map:
                return True
            else:
                n_map[num] = 1
        
        return False
        