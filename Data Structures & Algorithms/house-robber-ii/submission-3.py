class Solution:
    def rob(self, nums: List[int]) -> int:
        # Take the max of item 1 onwards, vs array without last item to prevent loop
        # must remember solution of only item 0 hence nums[0]
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
            