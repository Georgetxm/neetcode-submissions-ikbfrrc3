class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l = 0
        row_r = len(matrix) - 1
        row_mid = 0
        col_l = 0
        col_r = len(matrix[0]) - 1
        col_mid = 0

        while row_l <= row_r:
            row_mid = (row_l + row_r) // 2 

            if target == matrix[row_mid][0]:
                return True
            elif target > matrix[row_mid][-1]:
                row_l = row_mid + 1
            elif target < matrix[row_mid][0]:
                row_r = row_mid - 1
            else:
                break
                
        while col_l <= col_r:
            col_mid = (col_l + col_r) // 2

            if target == matrix[row_mid][col_mid]:
                return True
            elif target > matrix[row_mid][col_mid]:
                col_l = col_mid + 1
            elif target < matrix[row_mid][col_mid]:
                col_r = col_mid - 1
        
        return False

        
