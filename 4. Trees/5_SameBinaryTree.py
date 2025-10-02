# Same Binary Tree

# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]

# Output: true

# Example 2:

# Input: p = [4,7], q = [4,null,7]

# Output: false

# Example 3:

# Input: p = [1,2,3], q = [1,3,2]

# Output: false

# Constraints:

#     0 <= The number of nodes in both trees <= 100.
#     -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if (not p and q) or (p and not q):
                return False

            if p == q == None:
                return True
            elif p.val != q.val:
                return False

            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            if not left or not right:
                return False
            return True
        return dfs(p, q)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True

            if p and q and p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            else:
                return False
        return dfs(p, q)