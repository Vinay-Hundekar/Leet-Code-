# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        elif not list2:
            return list1
        head=ListNode()
        tail=head

        if list1.val<list2.val:
            tail.val=list1.val
            list1=list1.next
        else:
            tail.val=list2.val
            list2=list2.next

        while list1 and list2:
            tail.next=ListNode()
            tail=tail.next
            if list1.val<list2.val:
                tail.val=list1.val
                list1=list1.next
            else:
                tail.val=list2.val
                list2=list2.next
            
            
        while list1:
            tail.next=ListNode()
            tail=tail.next
            tail.val=list1.val            
            list1=list1.next
        while list2:
            tail.next=ListNode()
            tail=tail.next
            tail.val=list2.val
            list2=list2.next
        return head
