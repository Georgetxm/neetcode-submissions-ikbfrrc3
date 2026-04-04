class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == "0"):
                return

            grid[r][c] = "0"

            for d_r, d_c in directions:
                dfs(r + d_r, c + d_c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
