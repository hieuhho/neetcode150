# Invert Binary Tree

# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Example 1:

# Input: root = [1,2,3,4,5,6,7]

# Output: [1,3,2,7,6,5,4]

# Example 2:

# Input: root = [3,2,1]

# Output: [3,1,2]

# Example 3:

# Input: root = []

# Output: []

# Constraints:

#     0 <= The number of nodes in the tree <= 100.
#     -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # add root to stack
        stack = [root]

        while stack:
            # Take the last node added (DFS order)
            node = stack.pop()

            # Swap left and right children
            node.left, node.right = node.right, node.left

            # add the child nodes to process
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Return root (tree is inverted in place)
        return root
