# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half
        curr = slow.next
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        head1 = head
        head2 = prev
        # Break the half -1 link so the loop isnt circular
        # and terminate once head1 reaches none
        slow.next = None 

        # head2 has +1 element so we end it there
        while head2:
            new_next1 = head1.next
            new_next2 = head2.next

            head1.next = head2
            head2.next = new_next1

            head1 = new_next1
            head2 = new_next2
        
        return 
        