class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(filter(str.isalnum, s)).lower()

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            else:
                r -= 1
                l += 1
        
        return True
        