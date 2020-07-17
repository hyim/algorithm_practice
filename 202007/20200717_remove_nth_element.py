# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast_ptr = head
        slow_ptr = head
        count = 0
        while count < n:
            fast_ptr = fast_ptr.next
            count += 1
        count = 0
        while fast_ptr is not None and slow_ptr is not None:
            if fast_ptr.next is None:
                slow_ptr.next = slow_ptr.next.next
                return head
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        if fast_ptr is None:
            return slow_ptr.next
        return head
