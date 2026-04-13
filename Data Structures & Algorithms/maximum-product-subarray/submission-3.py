class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curr_max, curr_min = 1, 1


        for n in nums:
            temp = curr_max

            curr_max = max(n, n * curr_max, n * curr_min)
            curr_min = min(n, n * temp, n * curr_min)

            res = max(res, curr_max)

        return res
        
        