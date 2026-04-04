class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 2 Cases
        # Case 1. Even len "abba"
        # Case 2. Odd len "rac|e|car"

        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            l, r = i, i

            # Odd cases, think "rac|e|car"
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1


            l, r = i, i + 1

            # even cases, think "a|b||b|a"
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]



        