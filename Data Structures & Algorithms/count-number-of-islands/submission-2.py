class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if (r >= ROWS or r < 0 or
                c >= COLS or c < 0 or
                grid[r][c] == "0"):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
























        """ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))

            visited.add((r,c))

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while q:
                row, col = q.popleft()

                for diff_row, diff_col in directions:
                    new_row = row + diff_row
                    new_col = col + diff_col

                    if new_row >= 0 and new_row < ROWS:
                        if new_col >= 0 and new_col < COLS:
                            if grid[new_row][new_col] == "1":
                                if (new_row, new_col) not in visited:
                                    q.append((new_row, new_col))
                                    visited.add((new_row,new_col))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands""" 