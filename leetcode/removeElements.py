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
        prev = None
        curr = head
        
        while curr != None:
            if curr.val == val: #previous stays
                if curr == head: #remove head
                    head = curr.next
                else:               #remove node
                    prev.next = curr.next
            else: #previous changes
                prev = curr
            
            curr = curr.next
            
        return head
