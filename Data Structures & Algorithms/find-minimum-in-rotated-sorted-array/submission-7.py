class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        lowest = float('infinity')

        while l <= r:
            m = (l + r) // 2

            # left sorted
            if nums[m] >= nums[l]:
                lowest = min(lowest, nums[l])
                l = m + 1
            elif nums[m] <= nums[r]:
                lowest = min(lowest, nums[m])
                r = m - 1
        
        return lowest
            

        