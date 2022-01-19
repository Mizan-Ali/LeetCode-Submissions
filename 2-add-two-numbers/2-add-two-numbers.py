# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p, q = l1, l2
        dummyhead = ListNode(0)
        curr = dummyhead
        carry = 0
        
        while p != None or q != None:
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            
            res = x + y + carry
            carry = res//10
            curr.next = ListNode(res%10)
            curr = curr.next
            
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyhead.next
        