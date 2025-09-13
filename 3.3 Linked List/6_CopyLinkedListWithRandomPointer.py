# Copy Linked List with Random Pointer

# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

# Create a deep copy of the list.

# The deep copy should consist of exactly n new nodes, each including:

#     The original value val of the copied node
#     A next pointer to the new node corresponding to the next pointer of the original node
#     A random pointer to the new node corresponding to the random pointer of the original node

# Note: None of the pointers in the new list should point to nodes in the original list.

# Return the head of the copied linked list.

# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Example 1:

# Input: head = [[3,null],[7,3],[4,0],[5,1]]

# Output: [[3,null],[7,3],[4,0],[5,1]]

# Example 2:

# Input: head = [[1,null],[2,2],[3,2]]

# Output: [[1,null],[2,2],[3,2]]

# Constraints:

#     0 <= n <= 100
#     -100 <= Node.val <= 100
#     random is null or is pointing to some node in the linked list.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# for exammple:
# A'(7) ──→ B'(13) ──→ C'(11)
#   │         │          │
#   ▼         ▼          ▼
#  None      A'(7)      B'(13)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        # Seed with {None: None} so we can safely map .next/.random when they are None
        cloned_nodes = {None: None}
        # Pass 1: clone each original node, with no next/random map: {A: A (7), B: B(13), C: C(11)}
        current = head
        while current:
            cloned_nodes[current] = Node(current.val)
            current = current.next

        # Pass 2: assign next and random to the clones
        current = head
        while current:
            cloned_node = cloned_nodes[current]                             # clone of current
            cloned_node.next = cloned_nodes.get(current.next)               # set clone's .next | current.next = B => A.next = cloned_nodes['B'] = (B(13))
            cloned_node.random = cloned_nodes.get(current.random)           # set clone's .random | current.random = None => A.random = cloned_nodes[None] = None
            current = current.next
        return cloned_nodes[head]
