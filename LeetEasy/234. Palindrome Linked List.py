# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # slow is the pointer to point the half of the linked list
        # fast pointer is to traverse the linked list faster( twice the fast as slow pointer)
        slow=head
        fast=head
        # While loop to travesre the linked list
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # After the loop, slow points to half of the linked list
        # reverse is the link list which the reverse of the second half of the linked list
        reverse=self.reverselist(slow)

        # Traverse through the second half of the linked list
        while reverse:
            # Comparing the values of second half and first half values
            if reverse.val != head.val:
                # Returning false if they are not equal
                return False
            reverse=reverse.next
            head=head.next
        return True
    
    # Function to reverse the linked list
    def reverselist(self,head):
        prev=None
        while head:
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        # Returning the reversed linked list
        return prev
        