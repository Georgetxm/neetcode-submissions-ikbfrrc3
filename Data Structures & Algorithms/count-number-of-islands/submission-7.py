class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        islands = 0
        visited = set()

        def bfs(cell):
            r, c = cell
            q = deque()

            q.append((r, c))

            while q:
                r, c = q.popleft()
                visited.add((r, c))

                for dr, dc in DIRECTIONS:
                    new_r = r + dr
                    new_c = c + dc

                    if (new_r >= 0 and new_r < ROWS and
                        new_c >= 0 and new_c < COLS and
                        grid[new_r][new_c] == "1" and 
                        (new_r, new_c) not in visited):
                        q.append((new_r, new_c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs((r,c))

        return islands