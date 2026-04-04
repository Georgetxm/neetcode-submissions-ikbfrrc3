class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            # Iterate there are dupes
            # move left to progress the sliding window
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Adds new items to set regardless of dupes
            char_set.add(s[r])

            longest = max(longest, len(char_set))

        return longest
    
            
            
        