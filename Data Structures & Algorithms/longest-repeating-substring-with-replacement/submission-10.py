class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0] * 26

        l = 0
        longest = 0
        # valid: window - max(char) < k
        # invalid: move l
        for r in range(len(s)):
            window = (r - l) + 1
            r_idx = ord(s[r]) - ord('A')
            char_count[r_idx] += 1

            print(char_count)

            if window - max(char_count) > k:
                l_idx = ord(s[l]) - ord('A')
                char_count[l_idx] -= 1
                l += 1
            else:
                longest = max(longest, window)

        return longest