class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()


        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if i > 0 and num == nums[i - 1]:
                continue 
            

            left = i + 1
            right = len(nums)-1

            while left < right:
                rem = nums[i] + nums[left] + nums[right]

                if rem > 0:
                    right -= 1
                elif rem < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

    
        return res

            


