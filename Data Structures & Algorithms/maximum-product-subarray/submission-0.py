class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curr_max, curr_min = 1, 1

        for n in nums:
            # 3 Cases for each
            # Suppose array [1, 8, -2, -5]
            # At n = -2, curr_max = 8 (from prev n), curr_min = -2
            # At n = -5, curr_max = -5 * curr_min from prev iter (-2), curr_min = -4
            temp_max = curr_max
            curr_max = max(n, n * curr_max, n * curr_min)
            curr_min = min(n, n * temp_max, n * curr_min)

            res = max(res, curr_max)

        return res