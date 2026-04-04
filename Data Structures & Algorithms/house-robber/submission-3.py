class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        cum_rob = [0] * (len(nums))

        cum_rob[0] = nums[0]
        cum_rob[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cum_rob[i] = max(nums[i] + cum_rob[i-2], cum_rob[i - 1])

        return cum_rob[-1]
        