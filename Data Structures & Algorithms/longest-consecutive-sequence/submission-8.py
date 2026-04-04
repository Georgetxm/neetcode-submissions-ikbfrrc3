class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        items = set(nums)

        longest = 0

        for item in items:
            if (item - 1) not in items:
                current = 0
            
                while (item + current) in items:
                    current += 1

                longest = max(current, longest)


        return longest