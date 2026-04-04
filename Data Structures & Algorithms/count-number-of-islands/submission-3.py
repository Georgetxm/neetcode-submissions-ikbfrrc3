class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
            while q:
                row, col = q.popleft()
                for d_r, d_c in directions:
                    new_r = row + d_r
                    new_c = col + d_c
                    

                    if new_r >= 0 and new_r < ROWS:
                        if new_c >= 0 and new_c < COLS:
                            if (new_r, new_c) not in visited:
                                if grid[new_r][new_c] == "1":
                                    visited.add((new_r, new_c))
                                    q.append((new_r, new_c))

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)

        return islands