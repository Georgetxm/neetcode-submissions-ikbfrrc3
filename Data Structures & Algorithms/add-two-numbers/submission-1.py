# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                d1 = l1.val
                l1 = l1.next
            else:
                d1 = 0

            if l2:
                d2 = l2.val
                l2 = l2.next    
            else:
                d2 = 0

            total = d1 + d2 + carry
            
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)

            curr = curr.next
        

        return dummy.next
        

        