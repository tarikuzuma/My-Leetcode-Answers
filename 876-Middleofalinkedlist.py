

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Time complexity is O(n) where n is the number of nodes in the linked list
        # Space complexity is O(1)
        slow = head
        fast = head
        
        # Traverse the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow