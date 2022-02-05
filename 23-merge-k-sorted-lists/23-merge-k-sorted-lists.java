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
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Integer> minheap = new PriorityQueue<Integer>();
        for(ListNode node: lists) {
            while(node != null) {
                minheap.add(node.val);
                node = node.next;
            }
        }
        ListNode head = new ListNode(-1);
        ListNode tail = head;
        while(!minheap.isEmpty()) {
            tail.next = new ListNode(minheap.remove());
            tail = tail.next;
        }
        return head.next;
    }
}