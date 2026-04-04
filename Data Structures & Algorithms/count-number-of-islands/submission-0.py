class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while q:
                row, col = q.popleft()
                for diff_row, diff_col in directions:
                    new_row, new_col = row + diff_row, col + diff_col
                    if new_row >= 0 and new_row < rows:
                        if new_col >= 0 and new_col < cols:
                            if grid[new_row][new_col] == "1":
                                if (new_row, new_col) not in visited:
                                    q.append((new_row, new_col))
                                    visited.add((new_row, new_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)

        return islands

        