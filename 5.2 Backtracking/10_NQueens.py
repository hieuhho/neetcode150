# N-Queens
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

# A queen in a chessboard can attack horizontally, vertically, and diagonally.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

# You may return the answer in any order.

# Example 1:



# Input: n = 4

# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There are two different solutions to the 4-queens puzzle.

# Example 2:

# Input: n = 1

# Output: [["Q"]]
# Constraints:

# 1 <= n <= 8

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set() # r + c
        neg_diag = set() # r - c

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res