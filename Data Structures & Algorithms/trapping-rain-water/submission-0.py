class Solution:
    def trap(self, height: List[int]) -> int:
        breadth = len(height)
        left_wall = [0] * breadth
        right_wall = [0] * breadth
        area = 0

        for i in range(1, breadth):
            left_wall[i] = max(left_wall[i-1], height[i-1])

        for i in range(breadth-2, -1, -1):
            right_wall[i] = max(right_wall[i+1], height[i+1])
        
        for i in range(1, breadth-1):
            current = min(left_wall[i], right_wall[i]) - height[i]
            if current > 0:
                area += current

        return area
