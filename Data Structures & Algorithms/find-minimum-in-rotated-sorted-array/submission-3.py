class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Find the point at which the array has been "looped" around
        low = 0
        high = len(nums) - 1
        curr_min = float('inf')
        while low < high:
            mid = low + (high - low) // 2
            curr_min = min(curr_min, nums[mid])

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1


        return min(curr_min, nums[low])
        