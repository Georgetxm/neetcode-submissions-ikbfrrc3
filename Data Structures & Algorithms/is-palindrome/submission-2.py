class Solution:
    def isPalindrome(self, s: str) -> bool:
        isOdd = True if len(s) % 2 != 0 else False
        s = ''.join(filter(str.isalnum, s)).lower()

        l = 0
        r = len(s) - 1

        while l <= r:
            print(s[l], s[r])
            if isOdd and l == r:
                return True
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
