# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        prev=head
        prst=head.next
        while prst:
            if prev.val==prst.val:
                prev.next=prst.next
            else:
                prev=prst
            prst=prst.next
        
        return head
        