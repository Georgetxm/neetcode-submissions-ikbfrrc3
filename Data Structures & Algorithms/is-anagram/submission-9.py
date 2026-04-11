class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c_map = {}
        for c in s:
            c_map[c] = c_map.get(c, 0) + 1
        
        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        return t_map == c_map