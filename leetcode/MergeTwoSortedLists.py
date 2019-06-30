# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None: #two empty
            return None
        elif l1 is None:                # l1 empty
            ret = ListNode(l2.val)
            l2 = l2.next
        elif l2 is None:                #l2 empty
            ret = ListNode(l1.val)
            l1 = l1.next
        else:                           #both present
            if l1.val > l2.val:
                ret = ListNode(l2.val)
                l2 = l2.next
            else:
                ret = ListNode(l1.val)
                l1 = l1.next
                
        prev = ret
        while l1 is not None or l2 is not None:
            if l1 is None:
                curr = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                curr = ListNode(l1.val)
                l1 = l1.next
            else:
                if l1.val > l2.val:
                    curr = ListNode(l2.val)
                    l2 = l2.next
                else:
                    curr = ListNode(l1.val)
                    l1 = l1.next
            prev.next = curr
            prev = curr
        return ret
