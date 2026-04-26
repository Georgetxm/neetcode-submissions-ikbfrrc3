class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        
        for i in range(len(s)):
            # odd len
            l = r = i

            while l >=0 and r < len(s) and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1

            # even len 
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1

        return counter