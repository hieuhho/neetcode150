# Balanced Binary Tree

# Given a binary tree, return true if it is height-balanced and false otherwise.

# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:

# Input: root = [1,2,3,null,null,4]

# Output: true

# Example 2:

# Input: root = [1,2,3,null,null,4,null,5]

# Output: false

# Example 3:

# Input: root = []

# Output: true

# Constraints:

#     The number of nodes in the tree is in the range [0, 1000].
#     -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)         # maximum depth of this node

        return dfs(root) != -1
