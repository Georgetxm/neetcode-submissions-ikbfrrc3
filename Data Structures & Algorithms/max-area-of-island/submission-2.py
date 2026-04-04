class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            if (r >= ROWS or r < 0 or
                c >= COLS or c < 0 or 
                (r, c) in visited or 
                grid[r][c] == 0
                ):
                return 0

            visited.add((r, c))
            current_area = 1

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for d_r, d_c in directions:
                current_area += dfs(r + d_r, c + d_c)
            
            return current_area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(dfs(r, c), max_area)

        return max_area