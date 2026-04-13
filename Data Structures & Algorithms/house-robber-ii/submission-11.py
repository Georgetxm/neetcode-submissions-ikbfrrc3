class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[-1]

        def helper(nums):
            if not nums:
                return 0

            if len(nums) == 1:
                return nums[-1]

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])

            return dp[-1]

                
        return max(helper(nums[1:n]),
                    helper(nums[0:n-1]))
        
