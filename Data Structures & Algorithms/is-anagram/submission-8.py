from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = {}
        t_hash = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            s_hash[s_char] = s_hash.get(s_char, 0) + 1
            t_hash[t_char] = t_hash.get(t_char, 0) + 1

        if s_hash == t_hash:
            return True
        else:
            return False