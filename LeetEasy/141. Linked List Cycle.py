# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nxt=head
        while nxt and nxt.next:
            head=head.next
            nxt=nxt.next.next
            if head==nxt:
                return True
        return False