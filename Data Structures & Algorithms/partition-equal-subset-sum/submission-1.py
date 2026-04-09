class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = set()
        dp.add(0)

        for num in nums:

            nextDP = set()

            for item in dp:
                nextDP.add(item)
                new_item = item + num
                nextDP.add(new_item)

                if target in dp:
                    return True

            dp = nextDP


        return False
