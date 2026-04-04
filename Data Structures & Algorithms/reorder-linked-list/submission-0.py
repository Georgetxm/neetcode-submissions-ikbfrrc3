# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next # start with even index

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is currently at -1 index of the half item
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        head1 = head
        head2 = prev

        while head2:
            tmp1 = head1.next
            tmp2 = head2.next

            head1.next = head2
            head2.next = tmp1

            head1 = tmp1
            head2 = tmp2

        


        # # get length
        # nodes_len = 0
        # head_dupe = head
        # while head_dupe:
        #     nodes_len += 1
        #     head_dupe = head_dupe.next

        # mid = nodes_len // 2

        # h1_head = h2_head = head

        # for i in range(mid):
        #     h2_head = h2_head.next

        # h2_prev = None
        # h2_curr = h2_head

        # while h2_curr:
        #     nxt = h2_curr.next
        #     h2_curr.next = h2_prev
        #     h2_prev = h2_curr
        #     h2_curr = nxt

        # print(h2_prev)
        
        # for i in range(mid):
        #     nxt = h1_head.next
        #     h1_head.next = h2_prev
        #     nxt2 = h2_prev.next 
        #     h2_prev.next = nxt

        #     h1_head = nxt
        #     h2_prev = nxt2


