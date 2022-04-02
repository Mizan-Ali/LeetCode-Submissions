/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size = 0;
        ListNode ptr = head;
        
        while(ptr != null) {
            ptr = ptr.next;
            size++;
        }
        int t = size-n;
        if(t == 0)
            return head.next;
        
        ListNode ptr1 = head;
        for(int i=0; i<t-1; i++) {
            ptr1 = ptr1.next;
        }
        ptr1.next = ptr1.next.next;
        return head;
        
    }
}