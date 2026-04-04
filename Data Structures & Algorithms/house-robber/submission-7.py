class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i + 2) + nums[i], dfs(i + 1))

            return memo[i]

        return max(dfs(0), dfs(1))
