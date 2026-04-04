class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # List is sorted, don't iterate down the list further
            # all numbers are positive
            if num > 0:
                break

            if i > 0 and num == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                triplet = nums[i] + nums[l] + nums[r]
                if triplet > 0:
                    r -= 1
                elif triplet < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Iterate out the duplicates of the sorted list
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res
            


