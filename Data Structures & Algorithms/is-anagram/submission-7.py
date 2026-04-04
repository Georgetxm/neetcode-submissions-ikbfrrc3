from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        set_s = defaultdict(int)
        set_t = defaultdict(int)

        for item in range(len(s)):
            set_s[s[item]] += 1
            set_t[t[item]] += 1

        return set_s == set_t