class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashset = {}

        # for idx, n in enumerate(nums):
        #     rem = target - n

        #     if rem in hashset:
        #         return [hashset[rem], idx]
            
        #     hashset[n] = idx
        dupe = []

        for i, n in enumerate(nums):
            dupe.append([n, i])

        dupe.sort()
        
        i = 0
        j = len(dupe) - 1

        while i < j:
            curr_sum = dupe[i][0] + dupe[j][0]

            if curr_sum == target:
                return [min(dupe[i][1], dupe[j][1]),
                        max(dupe[i][1], dupe[j][1])]

            if curr_sum < target:
                i += 1
            elif curr_sum > target:
                j -= 1
        
        return [] 

        