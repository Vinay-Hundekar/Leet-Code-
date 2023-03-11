# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # This points to previous node
        prev=None
        while head:
            # Temp points to next node
            temp=head.next
            # Pointing the current node link to previous node
            # To change the direction
            head.next=prev
            # Updating the previous node to current Node
            prev=head
            # Updating current Node to next node
            head=temp
        # Returning the reversed Linkedlist
        return prev