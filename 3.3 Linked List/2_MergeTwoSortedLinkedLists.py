# Merge Two Sorted Linked Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]

# Example 2:

# Input: list1 = [], list2 = [1,2]

# Output: [1,2]

# Example 3:

# Input: list1 = [], list2 = []

# Output: []

# Constraints:

#     0 <= The length of the each list <= 100.
#     -100 <= Node.val <= 100

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node.
        # This avoids special cases for handling the head of the merged list.
        dummy = ListNode()

        # Tail always points to the *last* node in the merged list as we build it.
        # It starts at dummy and moves forward step by step.
        tail = dummy

        # While both lists still have nodes left, pick the smaller one.
        # Attach the smaller node to the merged list
        # Move list forward
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # Advance tail to the node we just attached,
            # so that the next insertion will happen after it.
            tail = tail.next


        # At least one list is now empty.
        # Attach the remainder of whichever list is not empty (list1 or list2).
        tail.next = list1 or list2

        # Return the merged list, which starts at dummy.next (skip the dummy itself).
        return dummy.next
