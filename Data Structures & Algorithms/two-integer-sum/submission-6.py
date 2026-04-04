class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [min(i, hashmap[diff]), max(i, hashmap[diff])]
            else:
                hashmap[num] = i

        print(hashmap)
        return []
        