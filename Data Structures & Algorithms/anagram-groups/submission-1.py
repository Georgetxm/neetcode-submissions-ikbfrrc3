class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i, s in enumerate(strs):
            char_list = [0] * 26

            for char in s:
                char_list[ord(char) - ord('a')] += 1

            key = tuple(char_list)
            hashmap[key].append(strs[i])

        res = []
        for values in hashmap.values():
            res.append(values)

        return res

        

        

        