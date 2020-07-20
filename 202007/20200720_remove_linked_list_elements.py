# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        first = head
        while first is not None and first.val == val:
            first = first.next
        
        prev = first
        if prev is None:
            return prev
        
        cur = prev.next
        if cur is None:
            return prev
        
        while cur is not None:
            if cur.val == val:
                prev.next = cur.next
                if first == cur:
                    first = prev.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return first
