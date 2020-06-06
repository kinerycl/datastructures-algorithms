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
        if head == None:
            return head
        
        nums = dict()
        
        curr = head
        while curr != None:
            if curr.val in nums:
                nums[curr.val] +=1
            else:
                nums[curr.val] = 1
            curr = curr.next
            
        prev = head
        #check head
        while nums[prev.val] > 1:
            head = prev.next
            prev = prev.next
            if prev == None:
                return None
            
        curr = prev.next
        
        while curr != None:
            if nums[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
