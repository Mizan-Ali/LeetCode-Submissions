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
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null) 
            return null;
        ListNode tail = head;
        int n = 1;
        while(tail.next != null) {
            n++;
            tail = tail.next;
        }
        int breakpt = n - (k%n);
        int i = 0;
        if(breakpt == n)
            return head;
        
        ListNode ptr = head, prev = head;
        while(i < breakpt) {
            i++;
            prev = ptr;
            ptr = ptr.next;
        }
        tail.next = head;
        head = ptr;
        prev.next = null;
        
        return head;
    }
}