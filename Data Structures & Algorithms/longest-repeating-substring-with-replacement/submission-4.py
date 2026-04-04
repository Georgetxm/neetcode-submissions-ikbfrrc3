class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0] * 26
        l = 0
        r = 0
        longest = 0

        for r in range(len(s)):
            window = (r - l) + 1
            char_count[ord(s[r]) - ord('A')] += 1

            # Invalid case where current window needs more 
            # replacement than k to form consecutive sequence
            if (window - max(char_count)) > k:
                char_count[ord(s[l]) - ord('A')] -= 1
                l = l + 1
            else:
                longest = max(longest, window)

        return longest

