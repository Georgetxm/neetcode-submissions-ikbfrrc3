class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_idx_map = defaultdict(list)
        
        for s_idx, s in enumerate(strs):
            c_count = [0] * 26

            for c in s:
                c_idx = ord(c) - ord('a')
                c_count[c_idx] += 1

            c_tup = tuple(c_count)
            str_idx_map[c_tup].append(s_idx)

        # print(str_idx_map)
        res = []
        for items in str_idx_map.values():
            cluster = [strs[item] for item in items]
            res.append(cluster)
        
        return res