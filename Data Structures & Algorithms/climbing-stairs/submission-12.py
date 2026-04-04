class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev, curr = 1, 2
        res = curr

        for i in range(3, n+1):
            prev, curr = curr, prev + curr
            res = curr

        return res