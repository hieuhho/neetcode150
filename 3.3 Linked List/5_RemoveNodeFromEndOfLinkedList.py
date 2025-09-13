# Remove Node From End of Linked List

# You are given the beginning of a linked list head, and an integer n.

# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:

# Input: head = [1,2,3,4], n = 2

# Output: [1,2,4]

# Example 2:

# Input: head = [5], n = 1

# Output: []

# Example 3:

# Input: head = [1,2], n = 2

# Output: [2]

# Constraints:

#     The number of nodes in the list is sz.
#     1 <= sz <= 30
#     0 <= Node.val <= 100
#     1 <= n <= sz

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node handles deletion of the head cleanly
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # 1) Create a gap of n between fast and slow
        for _ in range(n):
            fast = fast.next  # Given constraints, n is valid

        # 2) Walk both until fast is at the last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 3) Delete slow.next (the n-th from end)
        slow.next = slow.next.next

        # 4) Return the (possibly new) head
        return dummy.next