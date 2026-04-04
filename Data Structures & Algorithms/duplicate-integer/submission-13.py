class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            # At last element, do not compare any further
            if i == len(nums)-1:
                return False
            if nums[i] == nums[i+1]:
                return True

        return False
        # dupes={}
        # for num in nums:
        #     if num not in dupes:
        #         dupes[num] = 1
        #     else:
        #         return True

        # return False
         