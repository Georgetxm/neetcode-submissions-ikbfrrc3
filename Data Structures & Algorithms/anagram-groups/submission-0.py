class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                # Ascii lower a start at 97
                ascii_char = ord(c) - ord('a')
                count[ascii_char] += 1

            anagrams[tuple(count)].append(s)
        
        return list(anagrams.values())