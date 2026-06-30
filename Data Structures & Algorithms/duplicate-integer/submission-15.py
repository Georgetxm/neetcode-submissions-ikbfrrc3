class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = {}

        for n in nums:
            if n in hash_set:
                return True
            else:
                hash_set[n] = hash_set.get(n, 0) + 1

        

        return False