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

            r_start, r_end = res[-1]

            if start <= r_end:
                new_start = min(start, r_start)
                new_end = max(end, r_end)
                res[-1] = [new_start, new_end]
            else:
                res.append(inter)

        return res

            




        