# Count Good Nodes in Binary Tree
# Solved

# Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

# Given the root of a binary tree root, return the number of good nodes within the tree.

# Example 1:

# Input: root = [2,1,1,3,null,1,5]

# Output: 3

# Example 2:

# Input: root = [1,2,-1,3,4]

# Output: 4

# Constraints:

#     1 <= number of nodes in the tree <= 100
#     -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, high_val):
            if not node:
                return 0
            ans = 1 if node.val >= high_val else 0

            if node.val > high_val:
                high_val = node.val
            if node.left:
                ans += dfs(node.left, high_val)
            if node.right:
                ans += dfs(node.right, high_val)
            return ans
        return dfs(root, root.val)