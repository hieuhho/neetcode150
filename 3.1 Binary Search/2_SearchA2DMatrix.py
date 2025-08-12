# Search a 2D Matrix

# You are given an m x n 2-D integer array matrix and an integer target.

#     Each row in matrix is sorted in non-decreasing order.
#     The first integer of every row is greater than the last integer of the previous row.

# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Example 1:

# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

# Output: true

# Example 2:

# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

# Output: false

# Constraints:

#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 100
#     -10000 <= matrix[i][j], target <= 10000

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid_row = start + ((end - start) // 2)
            if matrix[mid_row][0] > target:
                end = mid_row - 1
            elif matrix[mid_row][-1] < target:
                start = mid_row + 1
            else:
                return target in matrix[mid_row]
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_len = len(matrix)
        columns_len = len(matrix[0])

        # this convert the 2D matrix to 1D
        start = 0
        end = rows_len * columns_len -1
        # then we just search the 1D matrix
        while start <= end:
            mid_of_matrix = start + (end - start) // 2
            row = mid_of_matrix // columns_len # how many rows we have passed
            col = mid_of_matrix % columns_len # how far into the row
            if target > matrix[row][col]:
                start = mid_of_matrix + 1
            elif target < matrix[row][col]:
                end = mid_of_matrix - 1
            else:
                return True
        return False

