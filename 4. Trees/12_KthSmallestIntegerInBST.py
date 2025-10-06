# Kth Smallest Integer in BST

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

# A binary search tree satisfies the following constraints:

#     The left subtree of every node contains only nodes with keys less than the node's key.
#     The right subtree of every node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees are also binary search trees.

# Example 1:

# Input: root = [2,1,3], k = 1

# Output: 1

# Example 2:

# Input: root = [4,3,5,2,null], k = 4

# Output: 5

# Constraints:

#     1 <= k <= The number of nodes in the tree <= 1000.
#     0 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        ans = root.val
        def dfs(node):
            if not node:
                return

            nonlocal count, ans
            dfs(node.left)
            count -= 1
            if count == 0:
                ans= node.val
                return
            dfs(node.right)

        dfs(root)
        return ans


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        while stack or current:
            while current:
                # add node to stack, go far left (smaller values)
                stack.append(current)
                current = current.left
            # popped node is smallest node in stack
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            # continue to right subtree
            current = current.right