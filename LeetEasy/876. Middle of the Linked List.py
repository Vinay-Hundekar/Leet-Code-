# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Function to find the middle of the linked list
    def middle(self,head):
        # Counter variable
        c=0
        while(head):
            head=head.next
            c+=1
        # c gives length, returning c//2 which is middle or half the length
        return c//2
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # m is middle of the linked list
        m=self.middle(head)
        # Moving head till middle
        for _ in range(m):
            head=head.next
        # Returning he head
        return head