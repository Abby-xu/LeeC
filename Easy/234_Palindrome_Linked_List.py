# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        Idea:
        use fast / slow pointers to find the middle node and see whether the list has odd/even number of elements.
        Reverse the right half the list, and compare with the left half
        
        E.g.
        1->2->3->4->3->2->1->null
        fast = null
        slow = 4
        slow->next = 3
        reverse(slow->next)
        null<-3<-2<-1 compare with 1->2->3->…

        Time complexity: O(n)
        Space complexity: O(1)
        '''
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
