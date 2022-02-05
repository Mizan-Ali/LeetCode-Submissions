from heapq import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        head = ListNode()
        tail = head
        
        for idx, node in enumerate(lists):
            if node != None:
                heappush(minheap, (node.val, idx))
        
        while minheap:
            val, id_ = heappop(minheap)
            tail.next = ListNode(val)
            tail = tail.next
            lists[id_] = lists[id_].next
            if lists[id_] != None:
                heappush(minheap, (lists[id_].val, id_))
        return head.next