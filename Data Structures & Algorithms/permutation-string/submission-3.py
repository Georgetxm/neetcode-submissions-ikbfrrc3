class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] += 1
            s2_count[ord(s2[i])-ord('a')] += 1

        if s1_count == s2_count: return True

        window = len(s1)

        for r in range(window, len(s2)):
            s2_count[ord(s2[r]) - ord('a')] += 1
            s2_count[ord(s2[r-window]) - ord('a')] -= 1
            
            if s1_count == s2_count: return True

        return False
