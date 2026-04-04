class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (target - pos)/speed

        pair = [[p,s] for p, s in zip(position, speed)]

        stack = []
        # Reverse sorted order
        # Because a car can only form a fleet with cars ahead of it

        for p, s in sorted(pair)[::-1]: 
            stack.append((target - p)/s)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)