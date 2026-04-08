class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0] * 26
        longest = 0
        l = 0

        for r in range(len(s)):
            window = (r - l) + 1
            char_count[ord(s[r]) - ord('A')] += 1

            if (window - max(char_count) > k):
                char_count[ord(s[l]) - ord('A')] -= 1
                l += 1
            else:
                longest = max(longest, window)

        return longest

        