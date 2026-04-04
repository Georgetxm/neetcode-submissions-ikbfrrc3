class Solution:
    def trap(self, height: List[int]) -> int:
        breadth = len(height)
        max_left = [0] * breadth
        max_right = [0] * breadth
        area = 0

        for i in range(1, breadth):
            max_left[i] = max(max_left[i-1], height[i-1])

        for i in range(breadth-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        
        for i in range(1, breadth-1):
            current = min(max_left[i], max_right[i]) - height[i]
            if current > 0:
                area += current

        return area
