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
        if head == None or head.next == None:
            return True
        
        ptr1 = head
        ptr2 = head
        
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
           
        ptr2 = head
        ptr1 = self.reverse(ptr1)
        
        while ptr1:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return True
    
    def reverse(self, node):
        prev = None
        while node:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
            
        return prev
