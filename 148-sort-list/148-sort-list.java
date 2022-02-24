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
    public ListNode sortList(ListNode head) {
        if(head == null) 
            return head;
        List<ListNode> arr = new ArrayList<ListNode>();
        ListNode ptr = head;
        while(ptr != null) {
            arr.add(ptr);
            ptr = ptr.next;
        }
        arr.sort((a, b) -> a.val - b.val);
        
        for(int i=0; i<arr.size()-1; i++) {
            arr.get(i).next = arr.get(i+1);
        }
        arr.get(arr.size()-1).next = null;
        return arr.get(0);
    }
}