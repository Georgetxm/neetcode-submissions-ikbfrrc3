class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hashset:
                return [hashset[rem], i]
            hashset[nums[i]] = i

        


        