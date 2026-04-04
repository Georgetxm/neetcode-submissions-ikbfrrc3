class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            char_list = [0] * 26

            for c in s:
                idx = ord(c) - ord('a')
                char_list[idx] += 1

            key = tuple(char_list)
            hashmap[key].append(s)

        res = []
        for values in hashmap.values():
            res.append(values)

        return res