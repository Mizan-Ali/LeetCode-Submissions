# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        arr = []
        ptr = head
        while ptr != None:
            arr.append(ptr)
            ptr = ptr.next
        arr.sort(key = lambda x: x.val)
        
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        arr[len(arr)-1].next = None
        
        return arr[0]