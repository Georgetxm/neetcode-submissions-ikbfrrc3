class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_high = len(matrix)
        high = len(matrix[0])

        outer_low, outer_high = 0, outer_high - 1

        while outer_low < outer_high:
            outer_mid = (outer_low + outer_high) // 2
            if target > matrix[outer_mid][-1]:
                outer_low = outer_mid + 1
            elif target < matrix[outer_mid][0]:
                outer_high = outer_mid - 1
            else:
                break

        if not (outer_low <= outer_high):
            return False

        outer_mid = (outer_low + outer_high) // 2
        low, high = 0, high - 1
        while low <= high:
            mid = (low + high) // 2
            if target > matrix[outer_mid][mid]:
                low = mid + 1
            elif target < matrix[outer_mid][mid]:
                high = mid - 1
            else:
                return True

        return False

        # outer_low = 0
        # outer_high = len(matrix) - 1
        # outer_mid = ((outer_high - outer_low) + outer_low) // 2

        # while outer_low <= outer_high:
        #     low = 0
        #     high = len(matrix[0]) - 1
        #     mid = ((high - low) + low) // 2
        #     while low <= high:
        #         curr_value = matrix[outer_mid][mid]
        #         if curr_value == target:
        #             return True

        #         # Outside this inner array
        #         if curr_value < matrix[outer_mid][low]:
        #             outer_high = outer_mid + 1
        #             outer_mid = (outer_low + (outer_high - outer_low)) // 2
        #             break

                
        #         if curr_value > matrix[outer_mid][high]:
        #             outer_low = outer_mid - 1
        #             outer_mid = (outer_low + (outer_high - outer_low)) // 2
        #             break

        #         # Inside inner array (i.e. this "row")
        #         if curr_value < matrix[outer_mid][mid]:
        #             high = mid + 1
        #             mid = (low + (high - low)) // 2
                
                
        #         if curr_value > matrix[outer_mid][mid]:
        #             low = mid - 1
        #             mid = (low + (high - low)) // 2


        # return False      

                    
