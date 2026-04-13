class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, candidate, used, res):
            if (len(candidate)) == len(nums):
                res.append(candidate[:])
                return

            for num in nums:
                if num not in used:
                    used.add(num)
                    candidate.append(num)

                    backtrack(nums, candidate, used, res)

                    used.remove(num)
                    candidate.pop()

            return res


        res = []

        return backtrack(nums, [], set(), res)

