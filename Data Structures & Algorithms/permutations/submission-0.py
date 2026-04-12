class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        def dfs(nums, candidate, used, res):
            if len(candidate) == len(nums):
                res.append(candidate[:])
                return

            for num in nums:
                if num not in used:
                    used.add(num)
                    candidate.append(num)
                    dfs(nums, candidate, used, res)
                    candidate.pop()
                    used.remove(num)

            return res


        res = []
        
        dfs(nums, [], set(), res)

        return res