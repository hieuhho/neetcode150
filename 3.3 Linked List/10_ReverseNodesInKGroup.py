# Reverse Nodes in K-Group

# You are given the head of a singly linked list head and a positive integer k.

# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

# Return the modified list after reversing the nodes in each group of k.

# You are only allowed to modify the nodes' next pointers, not the values of the nodes.

# Example 1:

# Input: head = [1,2,3,4,5,6], k = 3

# Output: [3,2,1,6,5,4]

# Example 2:

# Input: head = [1,2,3,4,5], k = 3

# Output: [3,2,1,4,5]

# Constraints:

#     The length of the linked list is n.
#     1 <= k <= n <= 100
#     0 <= Node.val <= 100

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_K_val(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # reverse group
            previous, current = kth.next, group_prev.next
            while current != group_next:
                tmp = current.next
                current.next = previous
                previous = current
                current = tmp

            group_tmp = group_prev.next
            group_prev.next = kth
            group_prev = group_tmp
        return dummy.next

    def get_K_val(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current
