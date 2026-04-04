class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        cum = [0] * len(nums)
        cum[0] = nums[0]
        cum[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cum[i] = max(cum[i-1], nums[i] + cum[i-2])

        return cum[-1]
        