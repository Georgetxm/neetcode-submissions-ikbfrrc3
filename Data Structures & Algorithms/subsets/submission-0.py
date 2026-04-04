class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            # Don't append current item    
            backtrack(i + 1)

            # Appending current item
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return res
        