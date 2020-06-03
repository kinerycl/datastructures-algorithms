# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        
        while pA != pB:
            if pA == None:
                pA = headB
            else:
                pA = pA.next
            
            if pB == None:
                pB = headA
            else:
                pB = pB.next
                
        return pA
