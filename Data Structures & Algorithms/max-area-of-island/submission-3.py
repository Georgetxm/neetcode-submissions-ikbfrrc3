class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1

            while q:
                r, c = q.popleft()
                visited.add((r, c))

                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for d_r, d_c in directions:
                    new_r = r + d_r
                    new_c = c + d_c
                    if (new_r >= 0 and new_r < ROWS and
                        new_c >= 0 and new_c < COLS and
                        grid[new_r][new_c] == 1  and
                        (new_r, new_c) not in visited
                        ):
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
                        area += 1

            return area
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(bfs(r, c), max_area)

        return max_area