# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        nxt = head
        while curr != None and curr.next != None:
            prev.next = curr.next
            nxt = prev.next
            curr.next = nxt.next
            nxt.next = curr
            prev = curr
            curr = curr.next
        return dummy.next