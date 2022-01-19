# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        adrmap = {}
        idx = 0
        node = head
        while node != None:
            if node not in adrmap:
                adrmap[node] = idx
                idx += 1
                node = node.next
            else:
                return node                               
        return None