from collections import defaultdict

class Solution:
    def default_value():
        return 0

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s=defaultdict(self.default_value)
        map_t=defaultdict(self.default_value)

        for i in range(len(s)):
            if (s[i] in map_s):
                map_s[s[i]] += 1
            else:
                map_s[s[i]] = 1
            if (t[i] in map_t):
                map_t[t[i]] += 1
            else:
                map_t[t[i]] = 1

        if map_s == map_t:
            return True
        
        return False
            


