class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h how many hours to eat all banana
        # k rate of banana eating/h
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            k = (high + low) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/k)
            
            if hours > h:
                low = k + 1
            elif hours <= h:
                res = k
                high = k - 1

        return res






        