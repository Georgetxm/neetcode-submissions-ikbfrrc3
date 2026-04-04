class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)

        def recurse(n, memo):
            if memo[n] != 0:
                return memo[n]

            if n == 1:
                memo[n] = 1
                return 1
            elif n == 2:
                memo[n] = 2
                return 2
            else:
                memo[n] = recurse(n-1, memo) + recurse(n-2, memo)
            
            return memo[n]

        return recurse(n, memo)

#         if n == 1:
#             return 1

#         if n == 2:
#             return 2
        
#         ways = [0] * (n+1)
#         ways[1] = 1
#         ways[2] = 2

#         for i in range(3, n+1):
#             ways[i] = ways[i-1] + ways[i-2]
# =

#         return ways[n]
        