# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Setting slow and fast pointer
        slow=head
        fast=head
        while fast and fast.next:
            # Slow pointer increment by one node
            slow=slow.next
            # Fast pointer increment by two node
            fast=fast.next.next
            # If slow is equal to head than it is a cyclic linked list
            if fast==slow:
                # Again initialize slow to head
                slow=head
                # Flast will be equal to slow where cyclic link begins 
                # Hence return slow
                while fast != slow:
                    slow=slow.next
                    fast=fast.next
                return slow
        # If it is a not a cyclic linked list than return None
        return None