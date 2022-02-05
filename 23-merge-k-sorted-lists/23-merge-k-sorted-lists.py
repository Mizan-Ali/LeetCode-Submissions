from heapq import heapify, heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        head = ListNode(-1) 
        tail = head
        
        for idx, node in enumerate(lists):
            if node is not None:
                heappush(minheap, (node.val, id(node), node))
        
        while minheap:
            value, idx, node = heappop(minheap)
            tail.next = node
            tail = node
            
            if tail.next is not None:
                heappush(minheap, (tail.next.val, id(tail.next), tail.next))
        return head.next