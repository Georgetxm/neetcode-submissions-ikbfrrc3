class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_T = {}

        for char in t:
            count_T[char] = count_T.get(char, 0) + 1

        # Counts the unique item needed
        need = len(count_T)
        window = {}
        have = 0

        res = [-1, -1]
        resLen = float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # Keys are not deleted so we need to do the 2nd comparison
            if char in count_T and window[char] == count_T[char]:
                have += 1
        
            while have == need:
                # Update result if shorter
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]

                # Find next smallest window                
                window[s[l]] -= 1
                
                if s[l] in count_T and window[s[l]] < count_T[s[l]]:
                    have -= 1

                l += 1

        if resLen != float("infinity"):
            return s[res[0]:res[1]+1]
        else:
            return ""

