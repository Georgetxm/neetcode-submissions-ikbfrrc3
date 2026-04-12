# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy.next = head
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            new_next = curr.next
            curr.next = prev
            prev = curr
            curr = new_next

        head1 = head
        head2 = prev
        
        while head2:
            new_next1 = head1.next
            new_next2 = head2.next
            
            head1.next = head2
            head2.next = new_next1
            
            head1 = new_next1
            head2 = new_next2

        return