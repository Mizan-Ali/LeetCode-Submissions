# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head == None:
            return head
        tail = head
        n = 1
        
        while tail.next != None:
            n += 1
            tail = tail.next
        
        breakpt = n - (k%n)
        print(breakpt)
        if(breakpt == n):
            return head
        ptr, prev = head, head
        i = 0
        while i < breakpt:
            i += 1
            prev = ptr
            ptr = ptr.next
        
        tail.next = head
        head = ptr
        prev.next = None
        
        return head