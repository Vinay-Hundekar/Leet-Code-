# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Initialy previous node is set as Null
        prev=None
        # New node is used to traverse the linked list
        new=head
        while new:
            # Checking wether curent node value is equal to val
            # Than pointing previous node next to next node
            if new.val == val and prev:
                prev.next=new.next
                new=new.next
                continue
            # Checking if initial valuse are equal to val, 
            # Than pointing head to the next node
            elif new.val == val:
                head=head.next
                new=head
                continue
            # Pointing previous node to current node
            # And current node to next node, to traverse through the linked list
            prev=new
            new=new.next
        return head
        
            