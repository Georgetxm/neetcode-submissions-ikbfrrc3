class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        res = []

        intervals.sort()

        for inter in intervals:
            start, end = inter
            
            if len(res) < 1:
                res.append(inter)
                continue

            prev_s, prev_e = res[-1]

            if start <= prev_e:
                min_start = min(start, prev_s)
                max_end = max(end, prev_e)
                res[-1] = [min_start, max_end]
            else:
                res.append(inter)

        return res
            
