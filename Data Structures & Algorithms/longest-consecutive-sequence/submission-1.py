class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        items = set(nums)

        longest = 0
        
        for num in nums:
            if (num - 1) not in items:
                length = 0
            
                while num + length in items:
                    length += 1

                longest = max(length, longest)
        
        return longest

            

        