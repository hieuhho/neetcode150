# Add Two Numbers

# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

# The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Return the sum of the two numbers as a linked list.

# Example 1:

# Input: l1 = [1,2,3], l2 = [4,5,6]

# Output: [5,7,9]

# Explanation: 321 + 654 = 975.

# Example 2:

# Input: l1 = [9], l2 = [9]

# Output: [8,1]

# Constraints:

#     1 <= l1.length, l2.length <= 100.
#     0 <= Node.val <= 9

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # reverse the lists
#         # sum as you go forward

#         l1_rev = None
#         current = l1
#         while current:
#             temp = current.next
#             current.next = l1_rev
#             l1_rev = current
#             current = temp

#         l2_rev = None
#         current = l2
#         while current:
#             temp = current.next
#             current.next = l2_rev
#             l2_rev = current
#             current = temp

#         dummy = ListNode()
#         tail = dummy
#         while l1_rev:
#             tail.next = ListNode(l1_rev.val + l2_rev.val)
#             l1_rev = l1_rev.next
#             l2_rev = l2_rev.next
#             tail = tail.next
#         return dummy.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum_value = v1 + v2 + carry
            carry = sum_value // 10 # find the carry of the sum (15 -> 1)
            sum_value = sum_value % 10 # find the remainder of the sum (15 -> 5)
            tail.next = ListNode(sum_value)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tail = tail.next
        return dummy.next