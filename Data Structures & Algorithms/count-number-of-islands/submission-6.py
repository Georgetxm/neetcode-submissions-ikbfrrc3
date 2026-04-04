class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            if (r >= ROWS or r < 0 or
                c >= COLS or c < 0 or 
                (r, c) in visited or 
                grid[r][c] == "0"
                ):
                return 
                
            visited.add((r, c))

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for d_r, d_c in directions:
                bfs(r + d_r, c + d_c)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands