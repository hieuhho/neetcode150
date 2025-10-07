# Binary Tree Maximum Path Sum

# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

# The path sum of a path is the sum of the node's values in the path.

# Example 1:

# Input: root = [1,2,3]

# Output: 6

# Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

# Example 2:

# Input: root = [-15,10,20,null,null,15,5,-5]

# Output: 40

# Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

# Constraints:

#     1 <= The number of nodes in the tree <= 1000.
#     -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # use a list so we don't have to use nonlocal inside dfs
        ans = [root.val]
        def dfs(node):
            if not node:
                return 0

            left =  dfs(node.left)
            right = dfs(node.right)
            left_max = max(left, 0)
            right_max = max(right, 0)

            # update answer with sum of current node with left & right
            ans[0] = max(ans[0], node.val + left_max + right_max)
            # return max of current node sum
            return node.val + max(left_max, right_max)

        dfs(root)
        return ans[0]
