from heapq import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        heap = []
        heapify(heap)
        
        for node in lists:
            if node is not None:
                heappush(heap, (node.val, id(node), node))
        
        while heap:
            val, idx, node = heappop(heap)
            tail.next = node
            tail = node
            
            if tail.next is not None:
                heappush(heap, (tail.next.val, id(tail.next), tail.next))
        return head.next