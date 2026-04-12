class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            0: (),
            1: (),
            ...
            8: ()
        """
        rows_set = defaultdict(set)
        cols_set = defaultdict(set)
        """ {
             (0, 0): (),
             (0, 1): (),
             ...
             (3, 3): ()
        """
        grids_set = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board)):
                cell = board[r][c]
                grid_idx = (r // 3, c // 3)
                if cell == ".":
                    continue

                if cell in rows_set[r]:
                    return False
                if cell in cols_set[c]:
                    return False
                if cell in grids_set[grid_idx]:
                    return False

                rows_set[r].add(cell)
                cols_set[c].add(cell)
                grids_set[grid_idx].add(cell)

        return True