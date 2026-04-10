class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        freshs = 0
        rot_q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshs += 1
                elif grid[r][c] == 2:
                    rot_q.append((r, c))
                    visited.add((r, c))

        mins = 0

        while rot_q and freshs > 0:
            mins += 1
            for _ in range(len(rot_q)):
                r, c = rot_q.popleft()
                grid[r][c] = 2

                for dr, dc in DIRECTIONS:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1):
                        freshs -= 1
                        visited.add((nr, nc))
                        rot_q.append((nr, nc))

        if freshs > 0:
            return -1
        else:
            return mins