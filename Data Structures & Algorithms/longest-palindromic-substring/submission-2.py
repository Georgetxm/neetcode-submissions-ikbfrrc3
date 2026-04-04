class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp
        resLen = 0
        resIdx = 0

        n = len(s)

        dp = [[False] * n for _ in range(n)] # n x n square matrix

        # iterate from last to first
        for i in range(n-1, -1, -1):
            # At every iteration, find longest from i to last
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j - i + 1) > resLen:
                        resIdx = i
                        resLen = j - i + 1
        
        return s[resIdx:resIdx + resLen]
        

        # 2 pointers
        """res = ""
        resLen = 0

        for i in range(len(s)):
            
            # odd len
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
            # even len
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res"""


