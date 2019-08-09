# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Algorithm: Not using the propertiy of length
Test Case:
    [4,1,8,4,5]
    [5,0,1,8,4,5]
in the first iteration currA goes till end while currB is at second last. Then headB
is again copied to currA. So, currA and currB is pointing to same linked list now.
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        currA = headA
        currB = headB
        
        while currA != currB:
            if currA:
                currA = currA.next
            else:
                currA = headB
            
            if currB:
                currB = currB.next
            else:
                currB = headA
                
        return currA
