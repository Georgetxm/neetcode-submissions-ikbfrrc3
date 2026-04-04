class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left sorted, get min of nums[l] and lowest -> try to find right side for smaller
        # right sorted, get min of nums[m] and lowest -> try to find left side for smaller

        lowest = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                lowest = min(nums[l], lowest)
                l = m + 1
            elif nums[r] >= nums[m]:
                lowest = min(nums[m], lowest)
                r = m - 1

        return lowest