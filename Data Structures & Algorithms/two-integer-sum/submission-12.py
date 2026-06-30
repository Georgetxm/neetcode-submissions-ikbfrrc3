class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for idx, n in enumerate(nums):
            rem = target - n

            if rem in hashset:
                return [hashset[rem], idx]
            
            hashset[n] = idx


        print(hashset)


        